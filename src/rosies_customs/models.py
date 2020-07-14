from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/')

class Item(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    