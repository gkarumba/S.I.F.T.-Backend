# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Retailer(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length = 500)
    location = models.PointField()    
    rating = models.IntegerField()
    link = models.CharField()
    contacts = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name