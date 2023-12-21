import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, f1_score
import joblib

# Load the dataset
data_path = '/Users/AKooner/Desktop/coding/capstone1/Thyroid_Diff.xls'
thyroid_data = pd.read_excel(data_path)

# Encode categorical variables
label_encoders = {}
for column in thyroid_data.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    thyroid_data[column] = label_encoders[column].fit_transform(thyroid_data[column])

# Splitting the dataset into features and target variable
X = thyroid_data.drop('Thyroid Function', axis=1)
y = thyroid_data['Thyroid Function']

# Standardizing the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting the standardized data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Training Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Print performance metrics
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"F1 Score: {f1}")

# Save the model to a file
joblib.dump(model, 'logistic_regression_model.joblib')