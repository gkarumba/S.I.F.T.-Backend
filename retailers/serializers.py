from rest_framework import serializers
from .models import *

class RetailerSerializer(serializers.ModelSerializer):
    distance = serializers.CharField()
    def get_distance(self,obj):
       return obj.distance == 0
 
    class Meta:
       model = Retailer
       fields = ('id', 'image', 'name', 'description', 'location', 'rating', 'link', 'contacts', 'email','distance')

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id','image','name','description','price','stockAvailable', 'retailer',)

class UserlocationSerializer(serializers.Serializer):
    latitude = serializers.CharField(max_length=20)
    longitude = serializers.CharField(max_length=20)

