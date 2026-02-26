# 🩹 AnniHeal — AI-Powered Wound Infection Risk Monitor

## 🚀 The Problem
Post-surgical and diabetic wounds often become severely infected before visible symptoms (redness, swelling) appear, leading to delayed treatment and severe complications. Millions of patients suffer from diabetic foot ulcers or surgical site infections annually, costing billions and leading to severe complications like amputations. Current detection relies on visual inspection—which is often too late.

## 💡 The Solution (How it works)
AnniHeal is an IoT + Machine Learning system that detects wound infection risk in real time using a smart wearable patch.

- **Hardware:** Smart bandage integrating Temperature, Gas (VOC/Ammonia), and Moisture sensors.
- **AI / Software:** Machine learning model (Random Forest) analyzes the real-time wound micro-environment to detect anomalies and generate an "Infection Risk Score."
- **Output:** Live dashboard and instant phone alerts to patients and caregivers for early intervention.

## 🏆 Why it wins
✔ **Proactive vs Reactive:** Non-invasive, continuous monitoring catches infections *before* they are critically dangerous.
✔ **Hardware + AI Synergy:** Leverages cheap IoT sensors powered by advanced predictive AI.
✔ **Actionable Insight:** Real-time dashboard and instant mobile alerts for clinical staff/caregivers, enabling early intervention (e.g., proactive antibiotic administration or dressing changes).
✔ **Market Potential:** Solves a multi-billion dollar healthcare problem with scalable, low-cost sensor integration.
✔ **Strong Branding:** "AnniHealaters" branding is finalized and memorable.

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

## 📊 How It Works (Technical Flow)

1. Sensor readings (Temperature, Gas Index, Moisture) are entered manually or streamed from ESP32 hardware.
2. The Flask backend passes the values to the trained `RandomForestRegressor` model.
3. The model outputs a **risk score (0–100%)**.
4. The dashboard classifies the score:

| Risk Level | Score Range | Action |
|---|---|---|
| 🟢 Low Risk | 0 – 39% | Monitor normally |
| 🟡 Moderate Risk | 40 – 69% | Increase monitoring |
| 🔴 High Risk | 70 – 100% | Immediate attention! |

---

*AnniHeal · IoT-based Wound Monitoring System · Hackathon Pitch Version*
