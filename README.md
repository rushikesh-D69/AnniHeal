# 🩹 AnniHeal — AI-Powered Wound Infection Risk Monitor

AnniHeal is an IoT + Machine Learning system that detects wound infection risk in real time using a smart wearable patch. It reads temperature, gas index, and moisture data from sensors, feeds them into a trained Random Forest model, and displays an infection risk score (0–100%) on a web dashboard.

---

## 🚀 Features

- 📡 **IoT Sensor Integration** — Reads Temperature (°C), Gas Index, and Moisture (%) from ESP32-based hardware
- 🤖 **ML Prediction** — Random Forest Regressor trained on real wound-sensor data, outputs a 0–100% infection risk score
- 📊 **Live Web Dashboard** — Interactive Flask dashboard with gauge chart, bar chart, and sensor preview cards
- 🎨 **Dark Mode UI** — Responsive, glassmorphism-style interface with risk-level color coding

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Hardware | ESP32, Temperature Sensor, Gas Sensor, Moisture Sensor |
| ML Model | Python, scikit-learn (RandomForestRegressor) |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript, Chart.js |
| Data | Pandas, NumPy, Joblib |

---

## 📁 Project Structure

```
AnniHeal/
├── dashboard/
│   ├── app.py                  # Flask web application
│   ├── test_predict.py         # Script to test model predictions
│   └── templates/
│       └── index.html          # Dashboard UI (Jinja2 template)
├── ml_model/
│   ├── dataset_anniheal.csv    # Raw sensor dataset
│   ├── dataset_with_risk.csv   # Dataset with computed risk scores
│   ├── model_training.ipynb    # Jupyter notebook for model training
│   ├── training_notebook.ipynb # Alternative training notebook
│   └── trained_model.pkl       # Trained model (joblib serialized)
├── hardware/                   # ESP32 firmware / wiring diagrams
├── docs/                       # Documentation assets
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/rushikesh-D69/AnniHeal.git
cd AnniHeal
```

### 2. Install Python dependencies
```bash
pip install flask scikit-learn numpy pandas joblib
```

### 3. Run the dashboard
```bash
python dashboard/app.py
```

### 4. Open in browser
```
http://127.0.0.1:5000
```

---

## 🔬 How It Works

1. Sensor readings (Temperature, Gas Index, Moisture) are entered manually or streamed from ESP32 hardware.
2. The Flask backend passes the values to the trained `RandomForestRegressor` model.
3. The model outputs a **risk score (0–100%)**.
4. The dashboard classifies the score:

| Risk Level | Score Range | Action |
|---|---|---|
| ✅ Low Risk | 0 – 39% | Monitor normally |
| ⚠️ Moderate Risk | 40 – 69% | Increase monitoring |
| 🚨 High Risk | 70 – 100% | Immediate attention! |

---

## 📌 Feature Importance (Estimated)

| Feature | Importance |
|---|---|
| 🌡️ Temperature (°C) | ~52% |
| 💨 Gas Index | ~31% |
| 💧 Moisture (%) | ~17% |

---

## ⚠️ Notes

- The trained model (`trained_model.pkl`) was serialized with **scikit-learn 1.6.1**. If you're running a newer version, you may see a version mismatch warning — the model will still work but retraining is recommended for production use.
- This is a development server. For production deployment, use a WSGI server like **Gunicorn**.

---

## 👤 Author

**Rushikesh** — [GitHub](https://github.com/rushikesh-D69)

---

*AnniHeal · Powered by scikit-learn Random Forest · IoT-based Wound Monitoring System*
