from flask import Flask, request, jsonify, make_response
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

app = Flask(__name__)

# Add CORS headers to all responses
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow all origins
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Handle OPTIONS preflight requests
@app.route('/predict', methods=['OPTIONS'])
def handle_options():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Load the trained model and preprocessor
model = joblib.load('models/loan_approval_model.pkl')
preprocessor = joblib.load('models/preprocessor.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = pd.DataFrame([{
            'no_of_dependents': int(data['no_of_dependents']),
            'education': data['education'],
            'self_employed': data['self_employed'],
            'income_annum': float(data['income_annum']),
            'loan_amount': float(data['loan_amount']),
            'loan_term': int(data['loan_term']),
            'cibil_score': int(data['cibil_score']),
            'residential_assets_value': float(data['residential_assets_value']),
            'commercial_assets_value': float(data['commercial_assets_value']),
            'luxury_assets_value': float(data['luxury_assets_value']),
            'bank_asset_value': float(data['bank_asset_value'])
        }])

        # Clean input data
        input_data['education'] = input_data['education'].str.strip()
        input_data['self_employed'] = input_data['self_employed'].str.strip()

        X_processed = preprocessor.transform(input_data)
        prediction = model.predict(X_processed)[0]
        probability = model.predict_proba(X_processed)[0][1]

        result = 'Approved' if prediction == 1 else 'Rejected'
        return jsonify({
            'status': 'success',
            'prediction': result,
            'probability': float(probability)
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/')
def home():
    return jsonify({'message': 'Loan Approval Prediction API is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)