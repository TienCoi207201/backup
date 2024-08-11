from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.TextField(max_length=10, blank=True)
    age = models.IntegerField( default= 0,blank= True)
    address = models.TextField(max_length=200, blank= True, null= True)

class Product(models.Model):
    name = models.TextField(max_length = 20, blank=True)  
    price = models.DecimalField(decimal_places= 2, max_digits= 10, blank=True)  
    description = models.TextField(max_length= 200, blank=True)