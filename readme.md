# 🩺 WCE Colon Disease Classification | Deep Learning & Digital Pathology

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/Model-YOLOv8s_cls-FF9900?logo=ultralytics)
![FastAPI](https://img.shields.io/badge/API-Backend-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)

An end-to-end machine vision pipeline designed to classify colon diseases from Wireless Capsule Endoscopy (WCE) images. This project leverages a fine-tuned **YOLOv8 classification model**, served via a high-performance REST API, and visualized through an interactive medical dashboard.

Trained on the highly regarded [Curated Colon Dataset for Deep Learning](https://www.kaggle.com/datasets/francismon/curated-colon-dataset-for-deep-learning), this system aims to assist medical professionals by providing rapid, AI-driven pathological screening.

---

## 🚀 Key Features

* **Advanced Computer Vision:** Utilizes `yolov8s-cls.pt` for high-accuracy, real-time image classification of gastrointestinal anomalies.
* **Separation of Concerns:** Clean architecture splitting the AI inference engine (`API`) from the user interface (`Dashboard`).
* **Interactive Digital Pathology:** A user-friendly Streamlit dashboard that allows researchers to upload WCE images and receive instant diagnostic probabilities.
* **Scalable Backend:** Ready-to-deploy API for seamless integration into larger hospital management systems.

---

## 📂 Repository Structure

```text
WCE-Curated-Colon-Disease/
├── api/
│   └── main.py              # Backend REST API for model inference
├── dashboard/
│   └── app.py               # Interactive Streamlit frontend UI
├── training/
│   ├── train.ipynb          # Jupyter notebook for YOLOv8 model training & evaluation
│   └── yolov8s-cls.pt       # The fine-tuned model weights
├── requirements.txt         # Project dependencies
└── .gitignore

```

---

## 🛠️ Installation & Quick Start

Follow these steps to run the complete pipeline on your local machine.

### 1. Clone & Install Dependencies

Ensure you have Python installed, then set up the environment:

```bash
git clone https://github.com/Arya-azimi/WCE-Curated-Colon-Disease.git
cd wce-curated-colon-disease

# Install required packages
pip install -r requirements.txt
```

### 2. Launch the API Backend

The backend serves the YOLOv8 model and handles inference requests. Open a terminal and run:

```bash
cd api

# Run the API server (assuming FastAPI/Uvicorn or Flask)

uvicorn main:app --reload
```

*The API will typically be available at `http://localhost:8000`.*

### 3. Launch the Medical Dashboard

Open a **new terminal window**, keep the API running, and start the Streamlit UI:

```bash
cd dashboard
streamlit run app.py
```

*Access the interactive dashboard in your browser at `http://localhost:8501`.*

---

## 🔬 Dataset Reference

The model is trained on the **Curated Colon Dataset**, which contains annotated Wireless Capsule Endoscopy images categorized into different pathological classes (e.g., Normal, Polyp, Ulcer).
🔗 [View Dataset on Kaggle](https://www.kaggle.com/datasets/francismon/curated-colon-dataset-for-deep-learning)

---

*Architected and developed by [Arya Azimi*](https://www.google.com/search?q=https://github.com/Arya-azimi)
