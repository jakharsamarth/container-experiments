import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('mushrooms.csv')

data = load_data()

# Show dataset in the app
st.write("Mushroom Dataset", data.head())

# Features and target column
X = data.drop(columns=["class"])
y = data["class"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sidebar: Classifier selection
classifier_option = st.sidebar.selectbox("Select Classifier", ("SVM", "Logistic Regression", "Random Forest"))

# Initialize classifier
if classifier_option == "SVM":
    model = SVC(probability=True)
elif classifier_option == "Logistic Regression":
    model = LogisticRegression()
else:
    model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# Display the evaluation metrics
st.write(f"Confusion Matrix for {classifier_option}")
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
plt.title("Confusion Matrix")
st.pyplot()

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
st.write(f"ROC AUC for {classifier_option}: {roc_auc:.2f}")
plt.figure()
plt.plot(fpr, tpr, color="darkorange", lw=2, label="ROC curve (area = %0.2f)" % roc_auc)
plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
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
