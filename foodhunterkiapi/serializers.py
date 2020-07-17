from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Place, Cuisine, Rating
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        #ukryte haslo, wymagane haslo
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        #automatyczne tworzenie tokenu uztkownika
        token = Token.objects.create(user=user)
        return user, token
    
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'title', 'description', 'address', 'city', 'prices', 'image', 'contact', 'no_of_ratings','avg_ratings')

class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ('id', 'name', 'place')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'place', 'user', 'stars')