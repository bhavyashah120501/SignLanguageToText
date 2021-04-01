from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('text-to-asl/', views.textToAsl, name="textToAsl"),
    
]