# predictor/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='predict'),  # Default view for prediction
    path('result/', views.result, name='result'),  # View for displaying the result (if needed)
]
