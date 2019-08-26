from rest_framework import serializers
from .models import *

class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ('id', 'image', 'name', 'description', 'location', 'rating', 'link', 'contacts', 'email')

class ProductSerializer(serializers.ModelSerializer):
    # retailer = RetailerSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id','image','name','description','price','stockAvailable', 'retailer')

class UserlocationSerializer(serializers.Serializer):
    latitude = serializers.CharField(max_length=20)
    longitude = serializers.CharField(max_length=20)