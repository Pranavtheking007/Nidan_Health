from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from django import forms


class stroke(forms.Form):
    gender = forms.ChoiceField()
    ever_married = forms.ChoiceField()
    work_type = forms.ChoiceField()
    residence_type = forms.ChoiceField()
    smoking_status = forms.ChoiceField()
    age = forms.IntegerField()
    Hypertension = forms.IntegerField()
    heart_disease = forms.IntegerField()
    avg_glucose_level = forms.IntegerField()
    bmi = forms.IntegerField()

class heart(forms.Form):
    cp = forms.ChoiceField()
    ca = forms.ChoiceField()
    sex = forms.IntegerField()
    trestbps = forms.IntegerField()
    chol = forms.IntegerField()
    fbs = forms.IntegerField()
    restecg = forms.IntegerField()
    thalach = forms.IntegerField()
    exang = forms.IntegerField()
    oldpeak = forms.IntegerField()
    slope = forms.IntegerField()
    
class diabetes(forms.Form):
     BMI = forms.IntegerField()
     Age = forms.IntegerField()
     sex = forms.ChoiceField() 
     Income = forms.IntegerField()
     PhysHlth = forms.IntegerField()
     HighBP = forms.ChoiceField()
     HighChol = forms.ChoiceField()
     Smoker = forms.ChoiceField()
     Stroke = forms.ChoiceField()
     HeartDisease = forms.ChoiceField()
     PhysActivity = forms.ChoiceField()
     Veggies = forms.ChoiceField()
     HeavyAlcoholConsump = forms.ChoiceField()
     DiffWalk = forms.ChoiceField()

class diabetesmed(forms.Form):
    Gender = forms.ChoiceField()
    Age  = forms.IntegerField()
    Urea = forms.IntegerField()
    HbA1c = forms.IntegerField()
    Chol = forms.IntegerField()
    TG = forms.IntegerField()
    HDL  = forms.IntegerField()
    VLDL = forms.IntegerField()
    BMI = forms.IntegerField()
