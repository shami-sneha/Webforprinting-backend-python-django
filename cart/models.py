from django.db import models
from django.contrib.auth.models import User
from orders.models import Orders
from products.models import Products
from photos.models import Photos
from documents.models import Documents


class Cart(models.Model):   
	userid = models.ForeignKey(Orders, on_delete=models.CASCADE,null=True )   
	status = models.FloatField(null=True) 

class CartItem(models.Model):
    cartid = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True ) 
    productid =  models.ForeignKey(Products, on_delete=models.CASCADE,null=True )  
    photoid= models.ForeignKey(Photos, on_delete=models.CASCADE,null=True,blank=True) 
    documentid = models.ForeignKey(Documents, on_delete=models.CASCADE,null=True,blank=True)

