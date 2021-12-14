from django.urls import path
from django.conf.urls import url

from django.contrib import admin
from django.urls import path ,include

from . import views

# from rest_framework import routers

# router = routers.AuthRouter()

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
    path('dashboard/urban_livability', views.urban_livability, name = 'urban_livability'),
    path('dashboard/rtp', views.rtp, name = 'rtp'),
    path('dashboard/Tribal_Area_Maharashtra', views.Tribal_Area_Maharashtra, name = 'Tribal Area(Maharashtra)'),
    path('dashboard/fgis', views.map, name = 'map'),
    # path('dashboard/schools', views.schools, name = 'schools'),
    path('dashboard/chandrapurcfrgis', views.chandrapurcfrgis, name = 'chandrapurcfrgis'),
    path('dashboard/chandrapurruralgis', views.chandrapurruralgis, name = 'chandrapurruralgis'),

    path('dashboard/raigadgis', views.raigadgis, name = 'raigadgis'),
    # path('',include(router.urls)),
    

]
