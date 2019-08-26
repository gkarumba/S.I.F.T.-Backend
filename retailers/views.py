# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework import filters
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework.response import Response
# Create your views here.

longitude = 0
latitude = 0
user_location = Point(longitude, latitude, srid=4326)


class ProductsList(generics.ListCreateAPIView):
    search_fields = ['image', 'name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # print(queryset)
    
class GetSearcherLocation(generics.CreateAPIView):
    serializer_class = UserlocationSerializer
    
    def get_queryset(self):
        # return self.model.objects.filter(user=self.request.user)
        pass
    
    def post(self,request,*args,**kwargs):
        lat = request.data.get('latitude','')
        lon = request.data.get('longitude','')
        
        if lat is not None and lon is not None:
            latitude = float(lat)
            longitude = float(lon)
            # print(latitude)
            # print(longitude)
            user_location = Point(longitude, latitude, srid=4326)
            print(user_location)
            userLocation = [{'latitude':lat,'longitude':lon},]
            results = UserlocationSerializer(userLocation, many=True).data
            return Response(results)
        
