from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# UserModel(AbstracteUser):
# Create your models here.
# class Users(models.Model):
#     names=models.CharField(max_length=50)


class OilModel(models.Model):
    # names=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    oilPhoto=models.ImageField(upload_to='image_uploaded',blank=False)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    description1=models.CharField(max_length=150,blank=True)
    description2=models.CharField(max_length=100)
    description3=models.CharField(max_length=105)
    class Meta:
        ordering=['-updated','-created']
    def __str__(self):
        return self.name
class DrugsModels(models.Model):
    drugname=models.CharField(max_length=50)
    drugpicture=models.ImageField(null=True)
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    description1=models.TextField(max_length=70)
    description2=models.CharField(max_length=100)
    description3=models.CharField(max_length=105)
    def __str__(self):
        return self.drugname
    
class AerosalModels(models.Model):
    aerosalname=models.CharField(max_length=50)
    aerosalpicture=models.ImageField(null=True)
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    description2=models.CharField(max_length=100)
    description3=models.CharField(max_length=105)
    description1=models.TextField(max_length=70)
    def __str__(self):
        return self.aerosalname
    
class SoaplModels(models.Model):
    soapname=models.CharField(max_length=50)
    soappicture=models.ImageField(null=True)
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    description1=models.TextField(max_length=70)
    description2=models.CharField(max_length=100)
    description3=models.CharField(max_length=105)
    def __str__(self):
        return self.soapname
class BreadModels(models.Model):
    breadname=models.CharField(max_length=50)
    beardpicture=models.ImageField(null=True)
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    description1=models.TextField(max_length=70)
    description2=models.CharField(max_length=100)
    description3=models.CharField(max_length=105)
    def __str__(self):
        return self.breadname
# class SoapModel(models.Model):
    