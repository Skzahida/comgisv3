from django.urls import path
# from django.conf.urls import url

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
    path('dashboard/healthv2', views.healthv2, name = 'healthv2'),      
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
    path('dashboard/urban_nutrition', views.urban_nutrition, name = 'urban_nutrition'),
    path('dashboard/watergis', views.watergis, name = 'watergis'),
    path('dashboard/capt_wells', views.capt_wells, name = 'capt_wells'),
    path('dashboard/uploadwellpic', views.uploadwellpic, name = 'uploadwellpic'),
    path('dashboard/login',views.loginUser, name="login"),
    path('dashboard/logoutUser',views.logoutUser,name = 'logoutUser'),
    path('dashboard/profile',views.profile,name='profile'),
    path('dashboard/deletehh',views.deletehh,name="deletehh"),
    path('dashboard/aww_map',views.aww_map, name='aww_map'),
    path('dashboard/addhh',views.addhh,name="addhh"),
    path('dashboard/beneficiaries',views.beneficiaries, name='beneficiaries'),
    path('dashboard/events',views.events,name="events"),
    path('dashboard/createAww',views.createaww,name="createAww"),
    path('dashboard/deleteaww',views.deleteaww,name="deleteaww"),
    path('dashboard/supervisior',views.supervisior_map,name='supervisior_map'),
    path('dashboard/beneficiary_form/<int:id>',views.beneficiary_form,name='beneficiary_form')
    # path('',include(router.urls)),
    

]
