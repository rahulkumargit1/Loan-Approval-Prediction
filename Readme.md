Loan Approval Prediction
This project is a web-based application that predicts whether a loan application will be approved or rejected based on applicant data. It uses a logistic regression model trained on a loan approval dataset and is deployed locally using a Flask backend and a modern HTML/CSS/JavaScript frontend.

Project Structure
loan-approval-prediction/
├── app.py                    # Flask backend API
├── requirements.txt          # Python dependencies
├── static/                   # Frontend files
│   ├── index.html            # Main HTML page with input form
│   ├── css/
│   │   └── styles.css        # CSS styling for the frontend
│   └── js/
│       └── script.js         # JavaScript for form submission and API interaction
├── models/                   # Trained model and preprocessor files
│   ├── loan_approval_model.pkl  # Trained logistic regression model
│   └── preprocessor.pkl        # Preprocessor for feature scaling and encoding
├── data/
│   └── loan_approval_dataset.csv  # Dataset for training the model
├── notebooks/
│   └── loan-approval-prediction-analysis.ipynb  # Jupyter notebook for data analysis and model training
├── README.md                 # Project documentation
└── .gitignore                # Git ignore file

Features

Data Preprocessing: Handles numerical feature scaling and categorical feature encoding using StandardScaler and OneHotEncoder.
Model Training: Uses a logistic regression model to predict loan approval (Approved or Rejected).
Web Interface: A modern, responsive form with a gradient background, organized sections, and hover effects.
API Endpoint: Flask API at /predict for processing input data and returning predictions with probabilities.
Visualization: Notebook includes confusion matrix and ROC curve for model evaluation.

Prerequisites

Python 3.12 or later
Jupyter Notebook for running the analysis notebook
Git (optional, for cloning the repository)
A web browser (e.g., Chrome, Firefox) to access the frontend

Setup Instructions
1. Clone the Repository
git clone <repository-url>
cd loan-approval-prediction

Note: Replace <repository-url> with the actual URL of your repository, or copy the project files to your local machine if not using Git. For this setup, assume the project is at E:\dhanush.
2. Create a Virtual Environment
Create and activate a virtual environment to isolate dependencies:
python -m venv "E:\COLLEGEPROJECT\College Project\envs\MachineLearning"


Windows (PowerShell):& "E:\COLLEGEPROJECT\College Project\envs\MachineLearning\Scripts\Activate.ps1"



3. Create Directories
Ensure the required directories exist:
mkdir -p static/css static/js models data

4. Place the Dataset

Copy loan_approval_dataset.csv to the data/ directory at E:\dhanush\data.
The dataset should have the following columns:
loan_id (optional, dropped during preprocessing)
no_of_dependents (integer, e.g., 0–5)
education (categorical: Graduate or Not Graduate)
self_employed (categorical: Yes or No)
income_annum (float, annual income in INR)
loan_amount (float, loan amount in INR)
loan_term (integer, loan term in years)
cibil_score (integer, 300–900)
residential_assets_value (float, INR)
commercial_assets_value (float, INR)
luxury_assets_value (float, INR)
bank_asset_value (float, INR)
loan_status (categorical: Approved or Rejected)



5. Install Dependencies
Install the required packages within the virtual environment:
pip install -r requirements.txt

The requirements.txt contains:
flask==2.3.3
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.1
joblib==1.4.2

To install Jupyter Notebook (if not already installed):
pip install jupyter

6. Train the Model

Open notebooks/loan-approval-prediction-analysis.ipynb in Jupyter Notebook:jupyter notebook


Run all cells to:
Load and clean the dataset (handles whitespace and invalid loan_status values).
Preprocess features using StandardScaler for numerical features and OneHotEncoder for categorical features.
Train a logistic regression model.
Save the model and preprocessor to models/loan_approval_model.pkl and models/preprocessor.pkl.


Expected output:
Dataset shape: (4269, 13)
Cleaned loan_status values: ['Approved' 'Rejected']
Training shape: (3415, 11)
Testing shape: (854, 11)
Accuracy: ~0.90–0.95
Model and preprocessor saved successfully



7. Run the Flask Backend
Start the Flask API:
python app.py


The API will be available at http://localhost:5000.
Test the API by visiting http://localhost:5000/ (should return {"message": "Loan Approval Prediction API is running"}).

8. Run the Frontend
Serve the frontend files using Python’s HTTP server:
python -m http.server 8000 --directory static --bind 127.0.0.1


Open http://localhost:8000 in a web browser to access the input form.

Usage

Access the Web Interface:

Navigate to http://localhost:8000.
Fill out the form with applicant details, such as:
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




Submit the Form:

Click the "Predict Loan Status" button.
The result will display below the form, e.g., Prediction: Approved (Probability of Approval: 92.34%).


Test the API Directly (Optional):

Use a tool like Postman or curl to send a POST request to http://localhost:5000/predict with JSON data:{
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


Expected response:{
    "status": "success",
    "prediction": "Approved",
    "probability": 0.9234
}





Troubleshooting

FileNotFoundError for Dataset:
Ensure data/loan_approval_dataset.csv exists at E:\dhanush\data.
Update the path in the notebook if necessary (e.g., file_path = 'E:/dhanush/data/loan_approval_dataset.csv').


ValueError: Input y contains NaN:
Check the notebook output for df['loan_status'].unique().
If unexpected values appear (e.g., ' Approved', 'rejected'), the notebook’s cleaning steps should handle them. If not, add custom replacements in the notebook.


Model/Preprocessor Not Found:
Verify models/loan_approval_model.pkl and models/preprocessor.pkl exist at E:\dhanush\models.
Re-run the notebook to generate these files.


Frontend Errors:
Check the browser console (F12 → Console) for JavaScript errors.
Ensure the Flask backend is running at http://localhost:5000.


Low Model Accuracy:
The logistic regression model typically achieves ~0.90 accuracy. For better performance, consider trying other models (e.g., Random Forest) in the notebook or tuning hyperparameters (e.g., C in LogisticRegression).


Virtual Environment Issues:
Ensure Python 3.12 is installed and accessible (python --version).
If activation fails in PowerShell, run:Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned




Port Conflicts:
If port 5000 (backend) or 8000 (frontend) is in use, check:netstat -aon | findstr :5000
netstat -aon | findstr :8000
taskkill /PID <pid> /F


Or change ports in app.py (e.g., port=5001) and the frontend command (e.g., 8080).



Contributing

To contribute, fork the repository, make changes, and submit a pull request.
Report issues or suggest improvements via the GitHub issues tab.

Acknowledgments

Dataset: Loan Approval Dataset (update with exact source if known)
Libraries: Flask, Scikit-learn, Pandas, NumPy

License
This project is licensed under the MIT License.
Contact
For questions or support, contact the authors:

Rahul: [Insert email or GitHub link, if available]

