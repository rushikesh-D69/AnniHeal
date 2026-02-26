# AnniHeal  
AI-Enabled IoT Wound Infection Risk Monitoring System  
Hackathon / Research Prototype Version

---

## Overview

AnniHeal is an AI-powered IoT system designed to estimate early wound infection risk by analyzing micro-environmental changes using multi-sensor fusion and probabilistic modeling.

The system integrates:

- Embedded sensing (Temperature, Gas, Moisture)
- Machine learning-based regression modeling
- Real-time web dashboard visualization
- CPU-efficient inference on AMD Ryzen architecture

This project demonstrates a complete end-to-end pipeline from sensor acquisition to AI-based clinical decision support.

---

## Scientific Background

Wound infections, particularly in post-surgical and diabetic patients, often begin with subtle biochemical and physiological changes before visible clinical symptoms appear.

According to the World Health Organization (WHO), surgical site infections remain one of the most common healthcare-associated infections globally.

Early infection stages typically involve:

- Localized temperature elevation due to inflammatory response
- Increased volatile organic compound (VOC) emissions from bacterial metabolism
- Altered moisture levels caused by increased wound exudate

Visible symptoms such as redness, swelling, pain, and pus formation typically occur after microbial colonization has progressed.

AnniHeal focuses on detecting these pre-clinical micro-environment changes using multi-sensor fusion and AI-based pattern recognition.

---

## Problem Statement

Post-surgical and diabetic wounds often become severely infected before visible symptoms appear, leading to delayed treatment and serious complications.

Millions of patients suffer from:

- Diabetic foot ulcers
- Surgical site infections

These complications can result in:

- Extended hospital stays
- Increased treatment costs
- Amputations in severe cases

Current detection methods rely heavily on visual inspection and subjective clinical judgment, which is reactive rather than proactive.

---

## Proposed Solution

AnniHeal is an IoT + Machine Learning system that detects wound infection risk in real time using a smart wearable patch architecture.

### Hardware Layer

Simulated smart bandage integrating:

- Temperature sensor (DS18B20)
- Gas sensor (MQ-2 for VOC simulation)
- Moisture sensor (simulated via potentiometer)

Sensor readings are streamed from ESP32 hardware to a backend processing system.

### AI / Software Layer

A trained RandomForestRegressor analyzes sensor data patterns and outputs a continuous:

Infection Risk Score (0–100%)

The model performs multivariate regression over:

- Temperature drift
- Gas emission changes
- Moisture fluctuations

Instead of simple threshold detection, AnniHeal uses predictive modeling for probabilistic anomaly estimation.

### Output Layer

- Live monitoring dashboard
- Real-time risk visualization
- Risk stratification (Low / Moderate / High)

---

## System Architecture

Sensor Layer  
→ ESP32 Data Acquisition  
→ Serial Streaming (COM Port)  
→ Flask Backend  
→ RandomForestRegressor Inference  
→ Web Dashboard Visualization  

Refer to `docs/architecture.png` for architecture diagram.

---

## Technical Flow

1. Sensor readings are streamed from ESP32 via serial communication.
2. The Flask backend reads incoming values.
3. The trained RandomForestRegressor predicts infection probability.
4. The dashboard classifies risk:

| Risk Level | Score Range | Recommended Action |
|------------|------------|-------------------|
| Low        | 0 – 39%    | Routine monitoring |
| Moderate   | 40 – 69%   | Increased observation |
| High       | 70 – 100%  | Immediate medical attention |

---

## Dataset Methodology

Due to the lack of publicly available wound infection datasets combining temperature, gas emission, and moisture measurements, a controlled experimental dataset was generated.

Risk labels were derived using a physics-informed weighted probabilistic model based on:

- Normalized temperature deviation
- Gas concentration index
- Moisture variation

A logistic transformation was applied to produce continuous infection probability values.

This approach avoids arbitrary binary labeling and models infection as a progressive probabilistic process.

---

## Model Performance

Model: RandomForestRegressor  
Training Platform: AMD Ryzen 7 Processor  

Performance Metrics:

- R² Score: 0.9994721461911958  
- Mean Absolute Error (MAE): 0.1870117280811932  

The high R² score reflects accurate approximation of the controlled synthetic risk function.

Real-time inference latency is under 50 ms per prediction on CPU.

---

## Compute & Performance (AMD Architecture)

The model was trained and evaluated on an AMD Ryzen 7 processor, demonstrating efficient CPU-based machine learning performance without requiring dedicated GPU acceleration.

Key observations:

- Training completed in seconds for 100+ samples.
- Real-time inference is computationally lightweight.
- Architecture supports scalability to larger datasets on AMD-powered cloud infrastructure.

Future enhancements may include:

- ROCm-compatible GPU acceleration
- Time-series deep learning models
- Edge AI deployment via TinyML

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Hardware | ESP32, DS18B20, MQ-2 |
| ML Model | Python, scikit-learn (RandomForestRegressor) |
| Backend | Flask |
| Frontend | HTML, CSS |
| Data Processing | Pandas, NumPy |
| Model Persistence | Joblib |

---

## Innovation Highlights

- Probabilistic infection modeling instead of binary classification
- Multi-sensor fusion architecture
- Real-time IoT-to-AI pipeline
- CPU-efficient regression suitable for edge deployment
- Modular and scalable system design

---

## Setup & Run

1. Clone the repository
git clone https://github.com/rushikesh-D69/AnniHeal.git

cd AnniHeal


2. Install dependencies


pip install flask scikit-learn numpy pandas joblib


3. Run the dashboard


python dashboard/app.py


4. Open in browser


http://127.0.0.1:5000


---

## Future Work

- Clinical dataset validation
- Real-world wound monitoring trials
- Time-series modeling using LSTM/transformers
- Edge deployment on embedded platforms
- Integration with hospital monitoring systems

---

## Disclaimer

AnniHeal is a research prototype and decision-support system.

It is not a certified medical diagnostic device and requires clinical validation before deployment in h
