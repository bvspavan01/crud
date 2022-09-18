from pickle import TRUE
from django.db import models

class Employee(models.Model):
    eid=models.IntegerField(primary_key=TRUE)
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=20,default="ajmer")
    gender=models.CharField(max_length=20,default="male")
    vehicles=models.CharField(max_length=20,default="Car")
    image = models.ImageField(upload_to='images/',null=True, blank=True)