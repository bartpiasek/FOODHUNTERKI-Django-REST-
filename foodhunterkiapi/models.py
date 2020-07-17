from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Place(models.Model):
    PRICESRANGE = (
        (0, 'Low price'),
        (1, 'Medium price'),
        (2, 'High price')
    )
    
    title = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=50, default='Poznan')
    prices = models.IntegerField(choices=PRICESRANGE, null=True)
    image = models.ImageField(upload_to='placesimage/', height_field=None, width_field=None, max_length=None, default='Image')
    contact = models.URLField(('Facebook link'),max_length=80, unique=True, null=True)
    description = models.TextField(max_length=255, null=True)

    #number of ratings
    def no_of_ratings(self):
        ratings = Rating.objects.filter(place=self)
        return len(ratings)
    
    #avg of ratings
    def avg_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(place=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    #w admin wyswietla tytuly w tabeli zamiast object1,2 etc.
    def __str__(self):
        return self.title

#one to many - jedna kuchnia to wielu restauracji
class Cuisine(models.Model):
    name = models.CharField(max_length=50)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='characters')

    def __str__(self):
        return self.name
    



class Rating(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    
    class Meta:
        unique_together = (('user','place'),)
        index_together = (('user','place'),)