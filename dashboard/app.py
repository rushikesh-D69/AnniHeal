import os
import json
import threading
import time
import logging
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Optional: pyserial (graceful fallback if not installed)
try:
    import serial
    import serial.tools.list_ports
    SERIAL_AVAILABLE = True
except ImportError:
    SERIAL_AVAILABLE = False

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# ─── ML MODEL ──────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "..", "ml_model", "trained_model.pkl"))

# ─── SERIAL STATE ──────────────────────────────────────────────────────────────
_serial_lock = threading.Lock()
_serial_state = {
    "connected": False,
    "port": None,
    "temperature": None,
    "gas": None,
    "moisture": None,
    "last_update": None,
    "error": None,
}
_serial_thread = None
_serial_conn = None          # the serial.Serial object
_stop_event = threading.Event()


def _serial_reader(port: str, baud: int):
    """Background thread: reads JSON lines from the ESP32 serial port."""
    global _serial_conn
    _stop_event.clear()
    try:
        conn = serial.Serial(port, baud, timeout=2)
        _serial_conn = conn
        with _serial_lock:
            _serial_state["connected"] = True
            _serial_state["port"] = port
            _serial_state["error"] = None
        logging.info(f"[Serial] Connected to {port} @ {baud} baud")

        while not _stop_event.is_set():
            try:
                raw = conn.readline()
                if not raw:
                    continue
                line = raw.decode("utf-8", errors="ignore").strip()
                if not line:
                    continue
                data = json.loads(line)
                with _serial_lock:
                    _serial_state["temperature"] = data.get("temperature")
                    _serial_state["gas"] = data.get("gas")
                    _serial_state["moisture"] = data.get("moisture")
                    _serial_state["last_update"] = time.time()
            except json.JSONDecodeError:
                pass  # ignore non-JSON lines (boot messages etc.)
            except Exception as e:
                with _serial_lock:
                    _serial_state["error"] = str(e)
                    _serial_state["connected"] = False
                logging.warning(f"[Serial] Read error: {e}")
                break
        conn.close()
    except Exception as e:
        with _serial_lock:
            _serial_state["connected"] = False
            _serial_state["error"] = str(e)
        logging.warning(f"[Serial] Connect error: {e}")
    finally:
        _serial_conn = None
        with _serial_lock:
            _serial_state["connected"] = False
        logging.info("[Serial] Thread exited")


# ─── ROUTES ────────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    temp = float(request.form["temp"])
    gas = float(request.form["gas"])
    moisture = float(request.form["moisture"])

    input_data = pd.DataFrame(
        [[temp, gas, moisture]],
        columns=["temperatureC", "gas_index", "moisture_percent"]
    )
    prediction = model.predict(input_data)[0]

    if prediction < 40:
        status = "Low Risk"
        color = "green"
    elif prediction < 70:
        status = "Moderate Risk"
        color = "orange"
    else:
        status = "High Infection Risk"
        color = "red"

    return render_template(
        "index.html",
        result=round(prediction, 2),
        status=status,
        color=color
    )


@app.route("/serial/ports")
def serial_ports():
    """Return list of available COM ports."""
    if not SERIAL_AVAILABLE:
        return jsonify({"ports": [], "error": "pyserial not installed — run: pip install pyserial"})
    ports = [p.device for p in serial.tools.list_ports.comports()]
    return jsonify({"ports": ports})


@app.route("/serial/connect", methods=["POST"])
def serial_connect():
    """Start the serial reader thread for the requested port."""
    global _serial_thread, _stop_event

    if not SERIAL_AVAILABLE:
        return jsonify({"ok": False, "error": "pyserial not installed"}), 500

    body = request.get_json(force=True) or {}
    port = body.get("port", os.environ.get("SERIAL_PORT", ""))
    baud = int(body.get("baud", os.environ.get("SERIAL_BAUD", 115200)))

    if not port:
        return jsonify({"ok": False, "error": "No port specified"}), 400

    # Stop existing thread if running
    _stop_event.set()
    if _serial_thread and _serial_thread.is_alive():
        _serial_thread.join(timeout=3)

    _stop_event = threading.Event()
    _serial_thread = threading.Thread(
        target=_serial_reader, args=(port, baud), daemon=True
    )
    _serial_thread.start()

    # Give the thread a moment to connect
    time.sleep(0.8)
    with _serial_lock:
        state = dict(_serial_state)
    return jsonify({"ok": state["connected"], "error": state.get("error")})


@app.route("/serial/disconnect", methods=["POST"])
def serial_disconnect():
    """Stop the serial reader thread."""
    global _serial_conn
    _stop_event.set()
    if _serial_conn:
        try:
            _serial_conn.close()
        except Exception:
            pass
    with _serial_lock:
        _serial_state["connected"] = False
        _serial_state["temperature"] = None
        _serial_state["gas"] = None
        _serial_state["moisture"] = None
    return jsonify({"ok": True})


@app.route("/serial/data")
def serial_data():
    """Return the latest sensor reading from the ESP32."""
    with _serial_lock:
        return jsonify(dict(_serial_state))


@app.route("/serial/predict", methods=["POST"])
def serial_predict():
    """Run ML prediction on the latest live serial reading (for auto-predict)."""
    with _serial_lock:
        t = _serial_state["temperature"]
        g = _serial_state["gas"]
        m = _serial_state["moisture"]

    if t is None or g is None or m is None:
        return jsonify({"ok": False, "error": "No live data yet"}), 400

    input_data = pd.DataFrame(
        [[t, g, m]],
        columns=["temperatureC", "gas_index", "moisture_percent"]
    )
    prediction = float(model.predict(input_data)[0])

    if prediction < 40:
        status, color = "Low Risk", "green"
    elif prediction < 70:
        status, color = "Moderate Risk", "orange"
    else:
        status, color = "High Infection Risk", "red"

    return jsonify({
        "ok": True,
        "result": round(prediction, 2),
        "status": status,
        "color": color,
        "temperature": t,
        "gas": g,
        "moisture": m,
    })


# ─── AUTO-CONNECT ON STARTUP ───────────────────────────────────────────────────
def _try_auto_connect():
    port = os.environ.get("SERIAL_PORT")
    if port and SERIAL_AVAILABLE:
        baud = int(os.environ.get("SERIAL_BAUD", 115200))
        t = threading.Thread(target=_serial_reader, args=(port, baud), daemon=True)
        t.start()
        logging.info(f"[Serial] Auto-connecting to {port}")


if __name__ == "__main__":
    _try_auto_connect()
    app.run(debug=True, use_reloader=False)