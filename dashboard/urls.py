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
    path('dashboard/tdsc', views.tdsc, name = 'tdsc'),
    path('dashboard/thakkar_buppa_yojana', views.tby, name = 'thakkar_buppa_yojana'),
    path('dashboard/deonadi', views.deonadi, name = 'deonadi'),
    path('dashboard/pwss', views.pwss, name = 'pwss'),
    path('dashboard/edu', views.edu, name = 'edu'),

]