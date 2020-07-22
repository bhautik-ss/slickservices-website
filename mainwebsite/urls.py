"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainwebsite import views

app_name = "mainwebsite"

urlpatterns = [
    path('', views.home, name="index"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('careers/', views.careers, name="careers"),
    path('contactus/', views.contactus, name="contactus"),
    path('sendquery/', views.sendquery, name="sendquery"),
]
