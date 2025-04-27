# 🚀 Docker Experiment 2: Binary Classification WebApp with Streamlit

Welcome to **Docker Experiment 2**!  
This project demonstrates the use of Docker to containerize a machine learning web application built with **Streamlit**.  
The app classifies mushrooms as **edible** or **poisonous** based on user input, utilizing multiple machine learning models.

---

## 🚀 Project Overview

This project is a **Binary Classification WebApp** designed to predict mushroom edibility.  
It offers a choice between three classifiers:

- **Support Vector Machine (SVM)**
- **Logistic Regression**
- **Random Forest**

### Key Features:

- **Interactive Interface**: Built using Streamlit for easy interaction and visualization.
- **Multiple Classifiers**: Switch between different models seamlessly.
- **Evaluation Metrics**: View Confusion Matrix, ROC Curve, and Precision-Recall Curve.
- **Dockerized Deployment**: Simplified deployment in any environment.

---

## 📝 Prerequisites

Ensure you have the following installed before proceeding:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 📂 Project Structure

```
/Docker_Practices
 └── /Exp-2
     ├── Dockerfile                 # Dockerfile to build the image
     ├── docker-compose.yml         # Docker Compose configuration
     ├── app.py                     # Streamlit app for classification
     ├── requirements.txt           # Python dependencies
     └── mushrooms.csv              # Dataset used for classification
```

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/jakharsamarth/container-experiments.git
cd container-experiments/Exp-2
```

### Step 2: Build the Docker Image

```bash
docker-compose build
```

This command reads the `Dockerfile` and builds the container image.

### Step 3: Launch the Docker Container

```bash
docker-compose up
```

The application will now be accessible at [http://localhost:8501](http://localhost:8501).

### Step 4: Interact with the WebApp

- Open your browser and go to [http://localhost:8501](http://localhost:8501).
- Choose a classifier (SVM, Logistic Regression, or Random Forest) from the sidebar.
- Adjust hyperparameters and select evaluation metrics.
- Click **Classify** to see predictions and visualized metrics.

### Step 5: Stop the Application

```bash
docker-compose down
```

---

## 🧑‍💻 Helpful Docker Commands

- **View Running Containers**

```bash
docker ps
```

- **View Logs**

```bash
docker-compose logs
```

Or for a specific service:

```bash
docker-compose logs <service_name>
```

Example:

```bash
docker-compose logs dockerex2
```

- **Run Containers in Background**

```bash
docker-compose up -d
```

- **Stop All Containers**

```bash
docker-compose down
```

- **Stop a Specific Service**

```bash
docker-compose stop dockerex2
```

- **Rebuild and Restart**

```bash
docker-compose up --build
```

- **Clean Up Unused Resources**

```bash
docker system prune
```

Or only remove unused images:

```bash
docker image prune
```

---

## 🛠 Dockerfile Explained

The `Dockerfile` used in this project does the following:

- **Base Image**: Starts with a minimal `python:3-slim` image.
- **Environment Variables**: Prevents generation of `.pyc` files and ensures unbuffered output.
- **Install Dependencies**: Uses `requirements.txt`.
- **Set Working Directory**: `/app` inside the container.
- **Security**: Runs the app under a non-root user.
- **Expose Port**: Opens port `8501` (Streamlit default).
- **Run Command**: Starts the app with `streamlit run app.py`.

---

## 🧑‍💻 Python Dependencies

The project requires the following Python libraries:

- **pandas**: For data manipulation
- **streamlit**: For building the interactive UI
- **scikit-learn**: For model training and evaluation
- **matplotlib**: For plotting visualizations
- **seaborn**: For enhanced visualizations

---

## 🤝 Contributing

Contributions are welcome! 🚀  
Feel free to fork the repository, create a feature branch, and submit a pull request.  
If you find any bugs or have suggestions, please open an issue.

---

Happy Coding! 🎉

---

# 📜 Streamlit App Code (app.py)

```python
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache
def load_data():
    return pd.read_csv('mushrooms.csv')

data = load_data()

# Display dataset
st.write("Mushroom Dataset", data.head())

# Prepare features and target
X = data.drop(columns=["class"])
y = data["class"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sidebar for classifier selection
classifier_option = st.sidebar.selectbox("Select Classifier", ("SVM", "Logistic Regression", "Random Forest"))

# Model initialization
if classifier_option == "SVM":
    model = SVC(probability=True)
elif classifier_option == "Logistic Regression":
    model = LogisticRegression()
else:
    model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# Confusion Matrix
st.write(f"Confusion Matrix for {classifier_option}")
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
st.pyplot()

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
st.write(f"ROC AUC for {classifier_option}: {roc_auc:.2f}")
plt.figure()
plt.plot(fpr, tpr, color="darkorange", lw=2, label="ROC curve (area = %0.2f)" % roc_auc)
plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver Operating Characteristic")
plt.legend(loc="lower right")
st.pyplot()

# Precision-Recall Curve
precision, recall, _ = precision_recall_curve(y_test, y_proba)
st.write(f"Precision-Recall Curve for {classifier_option}")
plt.figure()
plt.plot(recall, precision, color="blue", lw=2, label="Precision-Recall curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.legend(loc="lower left")
st.pyplot()
```

---

# 📦 Dockerfile

```dockerfile
# Start from a minimal Python image
FROM python:3-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app
COPY . /app

# Create a non-root user
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Expose port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]
```

---

# 📋 requirements.txt

```
pandas
streamlit
scikit-learn
matplotlib
seaborn
```
