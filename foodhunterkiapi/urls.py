from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import PlaceViewSet, CuisineViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('place', PlaceViewSet)
router.register('cuisine', CuisineViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


