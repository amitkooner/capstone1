# Thyroid Function Prediction Project

Overview
This project focuses on predicting thyroid function using a dataset of clinicopathologic features related to well-differentiated thyroid cancer. The data was collected over a period of 15 years, with each patient being followed for at least 10 years. The goal is to use this dataset to develop a predictive model to assist healthcare providers in understanding and predicting thyroid cancer recurrence.

Files in the Repository
thyroid_final.py: This script contains the code for loading the dataset, preprocessing, training the Logistic Regression model, and saving the trained model.
app.py: A Flask application that serves as a web service for making predictions using the trained Logistic Regression model.
logistic_regression_model.joblib: The serialized Logistic Regression model ready for use in prediction.
README.md: This file provides an overview and instructions for the project.
Setup and Installation
Clone the Repository:
bash
Copy code
git clone https://github.com/your-username/your-repository.git
Install Required Libraries:
Ensure you have Python installed on your system.
Install the required libraries:
bash
Copy code
pip install pandas scikit-learn flask joblib
Download the Dataset:
Place your dataset file (e.g., Thyroid_Diff.xls) in the project directory.
Running the Model Training Script
Navigate to the project directory and run:
bash
Copy code
python thyroid_final.py
This will train the Logistic Regression model and save it as logistic_regression_model.joblib.
Using the Flask Application
Start the Flask application by running:
bash
Copy code
python app.py
The application will run on http://127.0.0.1:5000/.
To make predictions, send a POST request to http://127.0.0.1:5000/predict with the input features in JSON format.
Contributing
Contributions to this project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.


