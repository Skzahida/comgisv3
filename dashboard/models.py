# /home/ubuntu/myenv/comgisv3
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from pyexpat import model
from tarfile import REGULAR_TYPES
# from django.db import models
from django.contrib.gis.db import models
# from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper


role_list = role_list = [('Select','none'),('CDPO','CDPO'),('Supervisor','Supervisor'),('AWW','AWW')]
class User(forms.Form):
    username = forms.CharField(max_length = 200, widget=forms.TextInput(), required=True)
    password = forms.CharField(widget = forms.PasswordInput(), required=True)
    role = forms.CharField(label='Role',widget=forms.Select(choices=role_list),required=True)
# class IndiaFinal1617BasicLatlong(models.Model):
#     schcd = models.BigIntegerField(blank=True, null=True)
#     address = models.CharField(max_length=200, blank=True, null=True)
#     longitude = models.FloatField(blank=True, null=True)
#     latitude = models.FloatField(blank=True, null=True)
#     category = models.CharField(max_length=100, blank=True, null=True)
#     type_sch = models.CharField(max_length=100, blank=True, null=True)
#     management = models.CharField(max_length=100, blank=True, null=True)
#     distname = models.CharField(max_length=100, blank=True, null=True)
#     ac_year = models.CharField(max_length=100, blank=True, null=True)
#     school_name = models.CharField(max_length=100, blank=True, null=True)
#     block_name = models.CharField(max_length=100, blank=True, null=True)
#     cluster_name = models.CharField(max_length=100, blank=True, null=True)
#     village_name = models.CharField(max_length=100, blank=True, null=True)
#     pincode = models.FloatField(blank=True, null=True)
#     geom = models.TextField(blank=True, null=True)  # This field type is a guess.
#     states = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'india_final16_17_basic_latlong'
#         app_label = 'schooldb'

class Awc(models.Model):
    gid = models.IntegerField(blank=True, null=True)
    fid = models.AutoField(primary_key=True)
    beat_no = models.IntegerField()
    population = models.BigIntegerField()
    females = models.BigIntegerField()
    males = models.BigIntegerField()
    pregnant = models.BigIntegerField()
    regular = models.IntegerField()
    yrs0_6 = models.IntegerField()
    yrs6_11 = models.IntegerField()
    yrs11_18 = models.IntegerField()
    geom = models.PointField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        managed = False
        db_table = 'awc1'
