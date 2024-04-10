from django.db import models
from django.contrib.auth.models import User

COUNTRY_NAMES = (('India', 'India'), ('UK', 'UK'))
# Create your models here.

class States(models.Model):
    name = models.CharField(max_length=100)

class Country(models.Model):    
    countryname = models.CharField(max_length=100,choices= COUNTRY_NAMES )
    statename = models.ManyToManyField(States)    

class Address(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  
    countryid = models.CharField(max_length=100, choices=COUNTRY_NAMES , null=True)
    state = models.ForeignKey(States, on_delete=models.CASCADE, null=True)
    city = models.TextField(max_length=100,null=True)
    pincode = models.TextField(max_length=100, null=True)
    fullname = models.TextField(max_length=100, null=True)
    phonenumber = models.TextField(max_length=100, null=True)  
    addressline1 = models.TextField(max_length=100, null=True) 
    addressline2 = models.TextField(max_length=100, null=True, blank=True)
    instructions  = models.TextField(max_length=150, null=True, blank=True)
    lastmodifieddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)