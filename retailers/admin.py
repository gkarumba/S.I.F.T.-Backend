# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin

from .models import Retailer, Product
# Register your models here.
@admin.register(Product)
@admin.register(Retailer)

class RetailerAdmin(OSMGeoAdmin):
    list_display = ('name','id')
