from django.urls import path
from django.conf.urls import url

from django.contrib import admin
from django.urls import path ,include

from . import views

urlpatterns = [
    path('', views.HomePage, name = 'homepage'),
    path('dashboard/', views.Dash, name = 'dash'),
    path('dashboard/census', views.Census, name = 'census'),
    path('dashboard/health', views.health, name = 'health'),
    path('dashboard/edu', views.edu, name = 'edu'),

]