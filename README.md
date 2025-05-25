# 🧠 Ischemic Stroke Prediction Using Hybrid Deep Learning Models

This is a final-year academic project aimed at predicting the likelihood of ischemic stroke using a hybrid deep learning model that combines CNN and LSTM architectures. The system integrates a Django-based web frontend for user interaction and RESTful API endpoints for prediction, backed by trained deep learning models.

---

## 🚀 Objective

To build a robust, accurate, and interpretable prediction model for ischemic stroke using a combination of temporal and spatial health data.

---

## 📁 Project Structure

```
📆 stroke-prediction-deep-fusion
🔹 BACKEND/
🔹 └── Ischemic_Stroke.ipynb       # Model training & evaluation notebook (CNN, LSTM, CNN-LSTM)
🔹 FRONTEND/
🔹 ├── self/                       # Django project configuration
🔹 └── webapp/                     # Django app with views, templates, URLs
🔹 DATASET/                        # Stroke dataset CSV
🔹 cnn.pkl                         # Trained CNN model
🔹 lstm.pkl                        # Trained LSTM model
🔹 cnn_lstm.pkl                    # Trained CNN-LSTM hybrid model
🔹 requirements.txt                # Python dependencies
🔹 stroke-prediction-deep-fusion.pdf.pdf  # Full project documentation
```

---

## 🧠 Models Used

* **CNN**: Captures spatial patterns in structured/tabular data.
* **LSTM**: Models temporal health data dependencies.
* **CNN-LSTM**: Combines both for improved performance.

All models are trained and saved as `.pkl` files and can be loaded for predictions via Django views.

---

## 🌐 Frontend (Django Web App)

* **Homepage**: `index.html` – Welcome screen
* **Input Page**: `input.html` – Collects user health parameters
* **Result Page**: `output.html` – Displays stroke risk prediction

> The prediction logic is implemented using a `predict()` function inside `views.py`, which loads the appropriate `.pkl` model and returns the stroke risk prediction.

---

## 🔧 Backend Processing

* Data is collected from users via forms.
* Data is preprocessed (normalized, encoded).
* The selected model is used to generate a risk prediction.
* Output is rendered on `output.html`.

---

## 🛠️ Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

* Django 3.0.8
* pandas, numpy
* scikit-learn
* tensorflow, keras
* matplotlib, seaborn
* djangorestframework
* joblib, Pillow

---

## ⚙️ How to Run Locally

### 1. Clone and Setup Virtual Environment

```bash
git clone https://github.com/AnandKumar56/stroke-prediction-deep-fusion.git
cd stroke-prediction-deep-fusion
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Run the Django Frontend

```bash
cd FRONTEND
python manage.py migrate
python manage.py runserver
```

Access at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📊 Evaluation Metrics

| Model    | Training Accuracy | Validation Accuracy |
| -------- | ----------------- | ------------------- |
| CNN      | 92.35%            | 88.76%              |
| LSTM     | 84.40%            | 81.92%              |
| CNN-LSTM | 96.47%            | 94.53%              |

---

## 👥 Team Members

* **K. Goutham** – Model Implementation
* **K. Arun Kumar** – Frontend Developer
* **D. Anand Kumar** – Backend Developer
* **M. Jaswanth** – Data Research & Analysis

---

## 📄 Project Documentation

A detailed write-up of this project is available in the file [`stroke-prediction-deep-fusion.pdf`](./stroke-prediction-deep-fusion.pdf.pdf). It includes the system overview, model architectures, preprocessing steps, project structure, implementation logic, and testing considerations.

---

## 📄 License

This project is intended for academic use only.

---
