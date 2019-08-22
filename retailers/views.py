# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import filters

# Create your views here.
class ProductsList(generics.ListCreateAPIView):
   search_fields = ['image', 'name']
   filter_backends = (filters.SearchFilter,)
   serializer_class = ProductSerializer
   queryset = Product.objects.all()


