from django.contrib import admin
from .models import Place, Rating, Cuisine
# Register your models here.
admin.site.register(Place)
admin.site.register(Rating)
admin.site.register(Cuisine)