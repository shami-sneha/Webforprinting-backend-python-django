from django.db import models

class Documents(models.Model):
    docfile = models.FileField(upload_to='document/')
    docType = models.CharField(max_length=100, null=True)