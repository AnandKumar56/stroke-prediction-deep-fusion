from django.shortcuts import render
import numpy as np
from .models import predict


# Simple categorical encodings matching common label ordering used in stroke datasets
GENDER_MAP = {"female": 0, "male": 1, "other": 2}
MARRIED_MAP = {"no": 0, "yes": 1}
WORK_MAP = {
    "children": 0,
    "govt_job": 1,
    "government": 1,
    "never worked": 2,
    "never_worked": 2,
    "private": 3,
    "self-employed": 4,
    "self employed": 4,
}
RESIDENCE_MAP = {"rural": 0, "urban": 1}
SMOKING_MAP = {
    "formerly smoked": 0,
    "formerly_smoked": 0,
    "never smoked": 1,
    "never_smoked": 1,
    "smokes": 2,
    "unknown": 3,
}

CLASS_NAMES = ['No Stroke', 'Stroke']


def _encode(value, mapping, default=0):
    if value is None:
        return default
    key = value.strip().lower()
    return mapping.get(key, default)


def _to_scalar(pred):
    arr = np.array(pred)
    return float(arr.ravel()[0])


def home(request):
    return render(request, 'index.html')


def input(request):
    return render(request, 'input.html')


def output(request):
    gender = _encode(request.POST.get("gender"), GENDER_MAP)
    ever_married = _encode(request.POST.get("ever_married"), MARRIED_MAP)
    work_type = _encode(request.POST.get("work_type"), WORK_MAP)
    residence_type = _encode(request.POST.get("Residence_type"), RESIDENCE_MAP)
    smoking_status = _encode(request.POST.get("smoking_status"), SMOKING_MAP)

    age = float(request.POST.get("age"))
    hypertension = int(request.POST.get("hypertension"))
    heart_disease = int(request.POST.get("heart_disease"))
    avg_glucose_level = float(request.POST.get("avg_glucose_level"))
    bmi = float(request.POST.get("bmi"))

    features = [
        gender,
        age,
        hypertension,
        heart_disease,
        ever_married,
        work_type,
        residence_type,
        avg_glucose_level,
        bmi,
        smoking_status,
    ]

    algo = (request.POST.get('algo') or '').lower()
    y_pred = predict(features, algo)
    class_idx = int(round(_to_scalar(y_pred)))
    class_idx = max(0, min(class_idx, len(CLASS_NAMES) - 1))

    return render(request, 'output.html', {'out': CLASS_NAMES[class_idx]})
