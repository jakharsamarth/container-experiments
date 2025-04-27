# 🚀 Docker Experiment 10: Titanic Survival Predictor — Containerized Streamlit App 🚢

---

## 📌 Overview

The **Titanic Survival Predictor** is a machine learning web application that predicts whether a Titanic passenger would survive based on user input features.  
Built using **Python**, **scikit-learn**, **pandas**, and **Streamlit**, the app is fully **containerized using Docker** for seamless deployment and portability.

---

## 📂 Project Structure

```
Titanic-Prediction-Model/
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── main.py                # Streamlit app
├── titanic_model.py       # Model training script
└── titanic_model.pkl      # Trained model (serialized)
```

---

### 📜 File Descriptions

- **`main.py`** → Streamlit web app interface for user inputs and predictions.
- **`titanic_model.py`** → Script to train a Random Forest model and serialize it.
- **`titanic_model.pkl`** → Pre-trained ML model ready for inference.
- **`requirements.txt`** → List of required Python libraries.
- **`Dockerfile`** → Instructions to build the Docker image.

---

## 🤖 Model Training (`titanic_model.py`)

The model uses a **Random Forest Classifier** trained on the Titanic dataset. After training, the model is saved as `titanic_model.pkl` using `joblib` for efficient reuse.

### Training Workflow:
1. Load the Titanic dataset.
2. Handle missing values and encode categorical variables.
3. Train a Random Forest Classifier.
4. Save the trained model (`titanic_model.pkl`).

---

## 🎨 Streamlit Application (`main.py`)

The **Streamlit** app provides a clean, interactive interface where users input details like age, gender, fare, class, etc., and get an instant survival prediction.

### ✨ App Features:
- ✔️ User-friendly UI with Streamlit widgets.
- ✔️ Live predictions powered by the trained model.
- ✔️ Dropdowns, sliders, and inputs for better UX.

---

## 🐳 Docker Setup

To containerize the application, a **Dockerfile** is created for easy image building and deployment.

### 📄 Dockerfile

```dockerfile
# Use official slim Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY titanic_model.pkl titanic_model.pkl

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🚀 Running the Application with Docker

Follow these steps to build and run the app inside a Docker container:

### 1️⃣ Navigate to the Project Directory

```bash
cd Titanic-Prediction-Model
```

---

### 2️⃣ Build the Docker Image

```bash
docker build -t titanic-prediction .
```

---

### 3️⃣ Run the Docker Container

```bash
docker run -p 8501:8501 titanic-prediction
```

---

### 4️⃣ Access the Application

Open your browser and visit:

```
http://localhost:8501
```

![Streamlit Dashboard](https://github.com/user-attachments/assets/297b4705-aa32-4d0b-90d8-ac63f0a2e75e)

---

## 🎯 Conclusion

This project demonstrates how to deploy a **machine learning model** using **Streamlit** and **Docker**, making it **scalable**, **portable**, and **easy to run** across different environments.

---

## 🔥 Next Steps

- 🚀 Deploy the Dockerized app on **AWS EC2**, **GCP**, or **Vercel**.
- 🎨 Enhance the UI with **advanced Streamlit widgets** and **charts**.
- 🧠 Improve model performance with **feature engineering** and **hyperparameter tuning**.

