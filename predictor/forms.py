# predictor/forms.py

from django import forms

class LoanForm(forms.Form):
    gender = forms.ChoiceField(
        choices=[(1, 'Male'), (0, 'Female')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    married = forms.ChoiceField(
        choices=[(1, 'Yes'), (0, 'No')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    dependents = forms.ChoiceField(
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3+')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    education = forms.ChoiceField(
        choices=[(1, 'Graduate'), (0, 'Not Graduate')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    self_employed = forms.ChoiceField(
        choices=[(1, 'Yes'), (0, 'No')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    applicant_income = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    coapplicant_income = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    loan_amount = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    loan_amount_term = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    credit_history = forms.ChoiceField(
        choices=[(1, 'Yes'), (0, 'No')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    property_area = forms.ChoiceField(
        choices=[(2, 'Urban'), (1, 'Semiurban'), (0, 'Rural')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
