import os
from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Build path relative to this file so it works from any working directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "..", "ml_model", "trained_model.pkl"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    temp = float(request.form["temp"])
    gas = float(request.form["gas"])
    moisture = float(request.form["moisture"])

    # Feature order MUST match training: temperatureC, gas_index, moisture_percent
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

if __name__ == "__main__":
    app.run(debug=True)