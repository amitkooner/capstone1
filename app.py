from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained Logistic Regression model
model = joblib.load('logistic_regression_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)