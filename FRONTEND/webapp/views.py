from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from .models import predict  # Ensure predict function is properly defined

le = LabelEncoder()

class_names = ['No Stroke', 'Stroke']  # Adjust based on your classification labels

def home(request):
    return render(request, 'index.html')

def input(request):
    return render(request, 'input.html')

def output(request):
    # Extract and preprocess categorical features
    gender = request.POST.get("gender")
    gender = le.fit_transform([gender])
    
    ever_married = request.POST.get("ever_married")
    ever_married = le.fit_transform([ever_married])
    
    work_type = request.POST.get("work_type")
    work_type = le.fit_transform([work_type])
    
    residence_type = request.POST.get("Residence_type")
    residence_type = le.fit_transform([residence_type])
    
    smoking_status = request.POST.get("smoking_status")
    smoking_status = le.fit_transform([smoking_status])
    
    # Extract numerical features
    age = float(request.POST.get("age"))
    hypertension = int(request.POST.get("hypertension"))
    heart_disease = int(request.POST.get("heart_disease"))
    avg_glucose_level = float(request.POST.get("avg_glucose_level"))
    bmi = float(request.POST.get("bmi"))
    
    # Create input list
    lst = [gender[0], age, hypertension, heart_disease, ever_married[0], 
           work_type[0], residence_type[0], avg_glucose_level, bmi, smoking_status[0]]
    
    algo = request.POST.get('algo')
    out = predict(lst, algo)
    class_name = class_names[int(out)]
    
    return render(request, 'output.html', {'out': class_name})
