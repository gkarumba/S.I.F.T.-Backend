# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models

# Create your models here.
class Retailer(models.Model):
    image = models.ImageField(blank=True,)
    name = models.CharField(max_length=255)
    description = models.CharField(blank=True,max_length = 500)
    location = models.PointField()    
    rating = models.IntegerField(blank=True,default=2.5)
    link = models.CharField(blank=True,max_length = 500)
    contacts = models.IntegerField(blank=True,)
    email = models.EmailField(blank=True,)
    
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



