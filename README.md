# Loan Prediction App

This project is a Django-based web application that predicts loan approval based on various financial and personal parameters using multiple machine learning models. The application uses Logistic Regression, Random Forest, Gradient Boosting, and XGBoost classifiers to provide predictions.

## Table of Contents

- [Loan Prediction App](#loan-prediction-app)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Model Descriptions](#model-descriptions)
  - [Folder Structure](#folder-structure)
  - [Screenshots](#screenshots)
  - [Credits](#credits)

## Features

- User-friendly web interface to input personal and financial details.
- Validations to ensure all necessary fields are filled out correctly.
- Multiple machine learning models for loan prediction.
- Results displayed in an easy-to-understand format.

## Requirements

- Python 3.8 or higher
- Django 3.1 or higher
- scikit-learn
- xgboost
- joblib

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/loan-prediction-app.git
cd loan-prediction-app
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Apply the migrations:

```bash
python manage.py migrate
```

5. Load the pre-trained models into the appropriate directory:

```bash
mkdir -p predictor/models
# Copy your model files into predictor/models/
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open your browser and go to `http://127.0.0.1:8000/predictor/` to use the app.

## Usage

1. Enter the required details in the form on the main page.
2. Click on the "Predict" button to see the prediction results from the various models.
3. Review the predictions displayed on the results page.
4. Click "Try Again" to make another prediction.

## Model Descriptions

The application uses the following models for prediction:

1. **Logistic Regression** (`logistic_regression_model.pkl`): A simple linear model for binary classification.
2. **Random Forest Classifier** (`random_forest_classifier_model.pkl`): An ensemble method that uses multiple decision trees.
3. **Gradient Boosting Classifier** (`best_gb_clf_model.pkl`): An ensemble technique that builds models sequentially.
4. **XGBoost Classifier** (`best_xgb_clf_model.pkl`): An optimized gradient boosting library designed for speed and performance.

## Folder Structure

```
loan-prediction-app/
│
├── predictor/
│   ├── migrations/
│   ├── models/
│   │   ├── best_gb_clf_model.pkl
│   │   ├── best_log_reg_model.pkl
│   │   ├── best_rf_clf_model.pkl
│   │   ├── best_xgb_clf_model.pkl
│   │   ├── logistic_regression_model.pkl
│   │   ├── random_forest_classifier_model.pkl
│   │   ├── scaler.pkl
│   ├── templates/
│   │   └── predictor/
│   │       ├── predict.html
│   │       └── result.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── loan_prediction/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

## Screenshots

### Main Form Page
![Main Form Page](screenshots/main_form_page.png)

### Prediction Result Page Approved
![Prediction Result Page](screenshots/prediction_result_page.png)

### Prediction Result Page Failure
![Prediction Result Page Failure](screenshots/prediction_result_page_failure.png)

## Credits

- **Bootstrap** for the front-end framework.
- **scikit-learn** for the machine learning models.
- **xgboost** for the XGBoost model.
