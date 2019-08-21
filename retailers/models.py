# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models

# Create your models here.
class Retailer(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length = 500)
    location = models.PointField()    
    rating = models.IntegerField()
    link = models.CharField(max_length = 500)
    contacts = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length = 500)
    price = models.IntegerField()    
    stockAvailable = models.BooleanField()
    retailer = models.ForeignKey(Retailer,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



