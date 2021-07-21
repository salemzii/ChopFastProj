from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from store.models import Restaurant
from profiles.models import Customer


class Feedback(models.Model):
    title= models.CharField(max_length=50, blank=True)
    feedback = models.TextField()
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.feedback


class reportRestaurant(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, 
    related_name='restaurant') #Remove Fields blank and true when Restaurants become functional
    report = models.TextField()


    def __str__(self):
        return self.restaurant.name


# Create your models here.
