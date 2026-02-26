# 🩹 AnniHeal — AI-Powered Wound Infection Risk Monitor

---

##  Scientific Background

Wound infections, particularly in post-surgical and diabetic patients, often begin with subtle biochemical and physiological changes before visible clinical symptoms appear.

According to the World Health Organization (WHO), surgical site infections remain one of the most common healthcare-associated infections globally. Early infection stages involve:

-  Localized temperature elevation due to inflammatory response  
-  Increased volatile organic compound (VOC) emissions from bacterial metabolism  
-  Altered moisture levels caused by increased wound exudate  

Visible symptoms such as redness, swelling, pain, and pus formation typically occur **after** microbial colonization has progressed.

**AnniHeal focuses on detecting these pre-clinical micro-environment changes using multi-sensor fusion and AI-based pattern recognition.**

---

##  The Problem

Post-surgical and diabetic wounds often become severely infected before visible symptoms (redness, swelling) appear, leading to delayed treatment and severe complications.

Millions of patients suffer from:
- Diabetic foot ulcers  
- Surgical site infections  

These complications can result in:
- Extended hospital stays  
- High treatment costs  
- Amputations in severe cases  

Current detection methods rely heavily on visual inspection and subjective clinical judgment—which is often reactive rather than proactive.

---

##  The Solution (How it Works)

AnniHeal is an IoT + Machine Learning system that detects wound infection risk in real time using a smart wearable patch.

### 🩹 Hardware Layer
Smart bandage integrating:
-  Temperature sensor  
-  Gas sensor (VOC / Ammonia detection)  
-  Moisture sensor  

These sensors monitor the wound micro-environment continuously.

### 🧠 AI / Software Layer
A trained **Random Forest Regressor** analyzes sensor data patterns and outputs an:

> 📊 Infection Risk Score (0–100%)

The model performs multivariate analysis on:
- Temperature drift
- Gas emission changes
- Moisture fluctuations

Instead of simple threshold detection, AnniHeal uses predictive modeling for anomaly recognition.

### 📱 Output Layer
- Live monitoring dashboard  
- Real-time risk visualization  
- Phone alerts for patients and caregivers  

---


---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Hardware | ESP32, Temperature Sensor, Gas Sensor, Moisture Sensor |
| ML Model | Python, scikit-learn (RandomForestRegressor) |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript, Chart.js |
| Data Processing | Pandas, NumPy |
| Model Persistence | Joblib |

---

## 📊 How It Works (Technical Flow)

1. Sensor readings (Temperature, Gas Index, Moisture) are entered manually or streamed from ESP32 hardware.
2. The Flask backend passes the values to the trained `RandomForestRegressor` model.
3. The model outputs a **risk score (0–100%)**.
4. The dashboard classifies the score:

| Risk Level | Score Range | Recommended Action |
|---|---|---|
| 🟢 Low Risk | 0 – 39% | Routine monitoring |
| 🟡 Moderate Risk | 40 – 69% | Increased observation |
| 🔴 High Risk | 70 – 100% | Immediate medical attention |

---

## 🧪 Dataset Note

Currently, the model is trained on a controlled experimental dataset simulating wound micro-environment variations.  

Future work includes:
- Clinical data validation  
- Real-world wound monitoring trials  
- Expansion to time-series deep learning models  
- TinyML deployment for on-device inference  

---

## ⚙️ Setup & Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/rushikesh-D69/AnniHeal.git
cd AnniHeal
```

### 2️⃣ Install Python dependencies
```bash
pip install flask scikit-learn numpy pandas joblib
```

### 3️⃣ Run the dashboard
```bash
python dashboard/app.py
```

### 4️⃣ Open in browser
```
http://127.0.0.1:5000
```

---

##  Disclaimer

AnniHeal is a research prototype and decision-support system.  
It is **not a certified medical diagnostic device** and requires clinical validation before deployment in healthcare settings.

---

**AnniHeal · AI-Enabled IoT Wound Monitoring System · Hackathon / Research Prototype Version**
