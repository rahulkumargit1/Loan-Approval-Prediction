Loan Approval Prediction
<div align="center"> <img src="https://github.com/rahulkumargit1/acne-classification-system/blob/main/python.jpg" alt="Rahul Kumar's GitHub Cover" style="width: 100%; max-width: 800px; height: auto; border-radius: 10px;"> </div>
This web-based application predicts whether a loan application will be approved or rejected based on applicant data. It uses a logistic regression model trained on a loan approval dataset, with a Flask backend and a modern HTML/CSS/JavaScript frontend.
Project Structure
loan-approval-prediction/
├── app.py                          # Flask backend API
├── requirements.txt                # Python dependencies
├── static/                         # Frontend files
│   ├── index.html                  # Main HTML page with input form
│   ├── css/
│   │   └── styles.css              # CSS styling for the frontend
│   └── js/
│       └── script.js               # JavaScript for form submission and API interaction
├── models/                         # Trained model and preprocessor files
│   ├── loan_approval_model.pkl     # Trained logistic regression model
│   └── preprocessor.pkl            # Preprocessor for feature scaling and encoding
├── data/
│   └── loan_approval_dataset.csv   # Dataset for training the model
├── notebooks/
│   └── loan-approval-prediction-analysis.ipynb  # Jupyter notebook for data analysis and model training
├── README.md                       # Project documentation
└── .gitignore                      # Git ignore file

Features

Data Preprocessing: Scales numerical features using StandardScaler and encodes categorical features with OneHotEncoder.
Model Training: Employs a logistic regression model to predict loan approval status (Approved or Rejected).
Web Interface: Features a responsive form with a gradient background, organized sections, and hover effects.
API Endpoint: Flask API at /predict processes input data and returns predictions with probabilities.
Visualization: Includes a Jupyter notebook with a confusion matrix and ROC curve for model evaluation.

Prerequisites

Python 3.12 or later
Jupyter Notebook (for running the analysis notebook)
Git (optional, for cloning the repository)
Web browser (e.g., Chrome, Firefox) to access the frontend

Setup Instructions

Clone the Repository (or copy project files to E:\dhanush):
git clone https://github.com/rahulkumargit1/Loan-Approval-Prediction.git
cd loan-approval-prediction


Create a Virtual Environment:Create and activate a virtual environment:
python -m venv "E:\COLLEGEPROJECT\College Project\envs\MachineLearning"

Activate (Windows PowerShell):
& "E:\COLLEGEPROJECT\College Project\envs\MachineLearning\Scripts\Activate.ps1"


Create Directories:Ensure the required directories exist:
mkdir -p static/css static/js models data


Place the Dataset:Copy loan_approval_dataset.csv to E:\dhanush\data. The dataset should include:

loan_id (optional, dropped during preprocessing)
no_of_dependents (integer, 0–5)
education (Graduate or Not Graduate)
self_employed (Yes or No)
income_annum (float, annual income in INR)
loan_amount (float, loan amount in INR)
loan_term (integer, loan term in years)
cibil_score (integer, 300–900)
residential_assets_value (float, INR)
commercial_assets_value (float, INR)
luxury_assets_value (float, INR)
bank_asset_value (float, INR)
loan_status (Approved or Rejected)


Install Dependencies:Install required packages:
pip install -r requirements.txt

Contents of requirements.txt:
flask==2.3.3
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.1
joblib==1.4.2

Install Jupyter Notebook (if needed):
pip install jupyter


Train the Model:Open the Jupyter notebook:
jupyter notebook

Run all cells in notebooks/loan-approval-prediction-analysis.ipynb to:

Load and clean the dataset.
Preprocess features using StandardScaler and OneHotEncoder.
Train a logistic regression model.
Save the model and preprocessor to models/loan_approval_model.pkl and models/preprocessor.pkl.Expected output:

Dataset shape: (4269, 13)
Cleaned loan_status values: ['Approved' 'Rejected']
Training shape: (3415, 11)
Testing shape: (854, 11)
Accuracy: ~0.90–0.95
Model and preprocessor saved successfully


Run the Flask Backend:Start the Flask API:
python app.py

Access at http://localhost:5000. Test with http://localhost:5000/ (returns {"message": "Loan Approval Prediction API is running"}).

Run the Frontend:Serve the frontend:
python -m http.server 8000 --directory static --bind 127.0.0.1

Open http://localhost:8000 in a browser.


Usage

Access the Web Interface:

Navigate to http://localhost:8000.
Fill out the form with applicant details, e.g.:
Number of Dependents: 2
Education: Graduate
Self Employed: No
Annual Income: 9600000
Loan Amount: 29900000
Loan Term: 12
CIBIL Score: 778
Residential Assets Value: 2400000
Commercial Assets Value: 17600000
Luxury Assets Value: 22700000
Bank Asset Value: 8000000


Click "Predict Loan Status" to see the result (e.g., Prediction: Approved (Probability: 92.34%)).


Test the API Directly (Optional):Send a POST request to http://localhost:5000/predict with JSON:
{
    "no_of_dependents": 2,
    "education": "Graduate",
    "self_employed": "No",
    "income_annum": 9600000,
    "loan_amount": 29900000,
    "loan_term": 12,
    "cibil_score": 778,
    "residential_assets_value": 2400000,
    "commercial_assets_value": 17600000,
    "luxury_assets_value": 22700000,
    "bank_asset_value": 8000000
}

Expected response:
{
    "status": "success",
    "prediction": "Approved",
    "probability": 0.9234
}



Troubleshooting

FileNotFoundError for Dataset:Ensure data/loan_approval_dataset.csv is at E:\dhanush\data. Update the notebook path if needed (e.g., file_path = 'E:/dhanush/data/loan_approval_dataset.csv').

ValueError: Input y contains NaN:Check df['loan_status'].unique() in the notebook. If unexpected values appear (e.g., ' Approved'), the notebook’s cleaning steps should handle them. Otherwise, add custom replacements.

Model/Preprocessor Not Found:Verify models/loan_approval_model.pkl and models/preprocessor.pkl exist. Re-run the notebook to generate them.

Frontend Errors:Check the browser console (F12 → Console). Ensure the Flask backend is running at http://localhost:5000.

Low Model Accuracy:The model achieves ~0.90 accuracy. For better performance, try other models (e.g., Random Forest) or tune hyperparameters in the notebook.

Virtual Environment Issues:Verify Python 3.12 is installed (python --version). If activation fails in PowerShell:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned


Port Conflicts:If ports 5000 or 8000 are in use:
netstat -aon | findstr :5000
netstat -aon | findstr :8000
taskkill /PID <pid> /F

Or change ports in app.py (e.g., port=5001) and the frontend command (e.g., 8080).


Contributing
Fork the repository, make changes, and submit a pull request. Report issues or suggest improvements via the GitHub issues tab.
Acknowledgments

Dataset: Loan Approval Dataset (source TBD)
Libraries: Flask, Scikit-learn, Pandas, NumPy

License
This project is licensed under the MIT License.
Contact
For questions or support, contact:

Rahul: rahulkumargit1

