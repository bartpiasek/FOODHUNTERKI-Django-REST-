from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User 

from .models import Place, Cuisine, Rating
from .serializers import PlaceSerializer, CuisineSerializer, RatingSerializer, UserSerializer



# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    authentication_classes = (TokenAuthentication, )
    #permissions_classes = (IsAuthenticated, ) #z autoryzacja
    permissions_classes = (AllowAny, ) #bez autoryzacji
    
    #custom method
    @action(detail=True, methods=['POST'])
    def rate_place(self, request, pk=None):
        if 'stars' in request.data:

            place = Place.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            #user = User.objects.get(id=1)
            

            #rate place one method to two goals: if exist - update, if not exist -create new one
            #POST, PUT on one method
            try: 
                rating = Rating.objects.get(user=user.id, place=place.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except: #jesli ocena nie istnieje
                rating = Rating.objects.create(user=user, place=place, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            
        else:
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class CuisineViewSet(viewsets.ModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    authentication_classes = (TokenAuthentication, )
    permissions_classes = (IsAuthenticated, )

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permissions_classes = (IsAuthenticated, )

    #AKUTALIZACJA RATINGU
    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    #TWORZENIE RATINGU
    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
