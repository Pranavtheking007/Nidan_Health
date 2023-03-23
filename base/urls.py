from django.urls import path
from . import views
from django.contrib import admin
from django.http import HttpResponse



urlpatterns = [
    
    path('',views.login,name='home'),
    path('index.html',views.home),
    path('stroke.html',views.stroke,name = 'stroke'), 
    path('card.html',views.card),
    path('heartdisease.html',views.heart),
    path('diabetes.html',views.diabetes),
    path('diabetesmed.html',views.diabetesmed),
    path('mentalhealthstudents.html',views.mentalhlth),
    path('Result_Tp.html',views.stroke, name='stroke'),


    
]
