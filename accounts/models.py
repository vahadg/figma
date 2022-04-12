from django.db import models
from django.urls import reverse

# Create your models here.

class Locations(models.Model):
    location_name = models.CharField(max_length=100)
    location_image = models.ImageField()
    location_price = models.DecimalField(max_digits=20, decimal_places=2)
    location_text = models.TextField()
    location_likes = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.location_name

class Users(models.Model):
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_orders = models.ForeignKey('User_orders', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user_name

class User_orders(models.Model):
      order_price = models.DecimalField(max_digits=20, decimal_places=2)
      order_data = models.TextField()

class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):    
        return reverse('home')
