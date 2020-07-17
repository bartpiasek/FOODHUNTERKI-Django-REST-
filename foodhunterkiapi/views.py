from django.shortcuts import render
from rest_framework import viewsets

from .models import Place, Cuisine, Rating
from .serializers import PlaceSerializer, CuisineSerializer, RatingSerializer

# Create your views here.

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = (PlaceSerializer, )

class CuisineViewSet(viewsets.ModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = (CuisineSerializer, )

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = (RatingSerializer, )