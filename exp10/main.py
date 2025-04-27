# titanic_model.py

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load the dataset
data = pd.read_csv('titanic.csv')  # Make sure your CSV file is here
print("First 5 rows of the dataset:")
print(data.head())

# 2. Preprocess the data
# Fill missing values
data['Age'].fillna(data['Age'].mean(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

# Encode categorical columns
le_sex = LabelEncoder()
le_embarked = LabelEncoder()

data['Sex'] = le_sex.fit_transform(data['Sex'])       # Male=1, Female=0
data['Embarked'] = le_embarked.fit_transform(data['Embarked'])

# Select features and target
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = data[features]
y = data['Survived']

# 3. Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Build and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# 6. Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2f}")

# 7. Predict survival for a new passenger
def predict_passenger():
    print("\n--- New Passenger Survival Prediction ---")
    try:
        pclass = int(input("Enter Passenger Class (1/2/3): "))
        sex = input("Enter Sex (male/female): ").lower()
        age = float(input("Enter Age: "))
        sibsp = int(input("Enter Number of Siblings/Spouses Aboard: "))
        parch = int(input("Enter Number of Parents/Children Aboard: "))
        fare = float(input("Enter Fare Paid: "))
        embarked = input("Enter Port of Embarkation (C/Q/S): ").upper()

        # Encode inputs
        sex_encoded = le_sex.transform([sex])[0]
        embarked_encoded = le_embarked.transform([embarked])[0]

        # Create feature array
        passenger = [[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]]
        passenger_scaled = scaler.transform(passenger)

        prediction = model.predict(passenger_scaled)
        if prediction[0] == 1:
            print("\nPrediction: Survived ✅")
        else:
            print("\nPrediction: Did NOT Survive ❌")

    except Exception as e:
        print(f"Error: {e}")

# Call the function
predict_passenger()

