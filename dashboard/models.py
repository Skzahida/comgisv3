# /home/ubuntu/myenv/comgisv3
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from logging.config import _LoggerConfiguration
from operator import contains
from pyexpat import model
from tarfile import REGULAR_TYPES
from unittest.main import MAIN_EXAMPLES
# from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper

class UploadWellPictureModel(models.Model):
    picture = models.ImageField( upload_to='WellPics/', blank=True, null=True, default='WellPics/noImage.jpg')
    name = models.CharField(max_length=100, blank=True, null=True)
    well_nm = models.CharField(max_length=100, blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    lat = models.CharField(max_length=15)
    lng = models.CharField(max_length=15)
    def save(self, *args, **kwargs):
        if not self.id:
            self.picture = self.compressImage(self.picture)
        super(UploadWellPictureModel, self).save(*args, **kwargs)
    def compressImage(self,picture):
        imageTemproary = Image.open(picture)
        imageTemproary = imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        picture = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return picture
    class Meta:
       managed = True
# class CustomAccountManager(BaseUserManager):
#     def create_superuser(self, username, password, **other_fields):
#         default_ward = MumbaiWardBoundary2Jan2022.objects.get(id=1)
#         default_prabhag = MumbaiPrabhagBoundaries3Jan2022V2.objects.get(id=1)

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)
#         other_fields.setdefault('area','Ward')
#         other_fields.setdefault('designation','superuser')
#         other_fields.setdefault('Ward', default_ward)
#         other_fields.setdefault('prabhag', default_prabhag)
        
        
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')

#         return self.create_user(username,password,**other_fields)

#     def create_user(self, username,password,**other_fields):

#         # print(prabhag,Ward)
#         user = self.model(username=username, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user



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

class AwcSpecific(models.Model):
    asid = models.BigIntegerField(unique=True)
    geom = models.PointField()
    coverage = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    district = models.CharField(max_length=254)
    division = models.CharField(max_length=254)
    beat_no = models.BigIntegerField()
    area_id = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'awcspecific'

class Awc(models.Model):
    fid = models.AutoField(primary_key=True)
    beat_no = models.IntegerField()
    population = models.BigIntegerField()
    females = models.BigIntegerField()
    males = models.BigIntegerField()
    pregnant = models.BigIntegerField()
    lactating = models.BigIntegerField()
    regular = models.IntegerField()
    yrs0_6 = models.IntegerField()
    yrs6_11 = models.IntegerField()
    yrs11_18 = models.IntegerField()
    geom = models.PointField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    awc_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'awc1'



class HouseHolds(models.Model):
    hid = models.BigIntegerField()
    noofmembers = models.BigIntegerField()
    children = models.BigIntegerField()
    pregnant = models.BigIntegerField()
    lactating = models.BigIntegerField()
    yrs0_6 = models.BigIntegerField()
    yrs6_11 = models.BigIntegerField()
    yrs11_18 = models.BigIntegerField()
    males = models.BigIntegerField()
    females = models.BigIntegerField()
    geom = models.PointField()
    awc_id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        managed = False
        db_table = 'households'

class Aww(models.Model):
    awwid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=254)
    age = models.BigIntegerField()
    contact = models.CharField(max_length=254)
    awc_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'aww'


