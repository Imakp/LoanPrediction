# predictor/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoanForm
import joblib
import numpy as np

# Load the pre-trained models
log_reg_model = joblib.load('models/logistic_regression_model.pkl')
rf_model = joblib.load('models/random_forest_classifier_model.pkl')
best_gb_clf_model = joblib.load('models/best_gb_clf_model.pkl')
best_log_reg_model = joblib.load('models/best_log_reg_model.pkl')
best_rf_clf_model = joblib.load('models/best_rf_clf_model.pkl')
best_xgb_clf_model = joblib.load('models/best_xgb_clf_model.pkl')

def predict(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            gender = int(form.cleaned_data['gender'])
            married = int(form.cleaned_data['married'])
            dependents = int(form.cleaned_data['dependents'])
            education = int(form.cleaned_data['education'])
            self_employed = int(form.cleaned_data['self_employed'])
            applicant_income = float(form.cleaned_data['applicant_income'])
            coapplicant_income = float(form.cleaned_data['coapplicant_income'])
            loan_amount = float(form.cleaned_data['loan_amount'])
            loan_amount_term = float(form.cleaned_data['loan_amount_term'])
            credit_history = int(form.cleaned_data['credit_history'])
            property_area = int(form.cleaned_data['property_area'])

            # Compute additional features
            total_income = applicant_income + coapplicant_income
            emi = loan_amount / loan_amount_term

            # Create input array for the model
            input_features = np.array([[gender, married, dependents, education, self_employed,
                                        applicant_income, coapplicant_income, loan_amount, 
                                        loan_amount_term, credit_history, property_area,
                                        total_income, emi]])

            # Predict using each loaded model
            predictions = {
                'logistic_regression': log_reg_model.predict(input_features)[0],
                'random_forest': rf_model.predict(input_features)[0],
                'best_gb_clf': best_gb_clf_model.predict(input_features)[0],
                # 'best_log_reg': best_log_reg_model.predict(input_features)[0],
                # 'best_rf_clf': best_rf_clf_model.predict(input_features)[0],
                'best_xgb_clf': best_xgb_clf_model.predict(input_features)[0]
            }

            # Translate predictions into readable results
            result = {model: 'Approved' if prediction == 1 else 'Rejected'
                      for model, prediction in predictions.items()}

            return render(request, 'predictor/result.html', {'result': result})

    else:
        form = LoanForm()

    return render(request, 'predictor/predict.html', {'form': form})

def result(request):
    # This view function can serve as a placeholder or for debugging purposes
    return HttpResponse("This is the result view.")
