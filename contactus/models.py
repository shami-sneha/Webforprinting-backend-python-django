from django.db import models

# Create your models here.

class Contactus(models.Model):  
    fullname = models.TextField(max_length=100, null=True)
    email = models.TextField(max_length=100, null=True)      
    enquiryabout = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)    
    lastmodifieddate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email