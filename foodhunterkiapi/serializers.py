from rest_framework import serializers
from .models import Place, Cuisine, Rating

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'title', 'description','address','city','prices','image','contact','description')

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'place')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'place', 'users', 'stars')