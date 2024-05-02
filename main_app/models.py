from django.db import models
from user.models import User

class Practice(models.Model):
    dietitian = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length = 150)
    addressStreetNumberName = models.CharField(max_length = 100)
    addressSuburb = models.CharField(max_length = 50)
    addressCity = models.CharField(max_length = 50) 
    addressState = models.CharField(max_length = 50)
    addressCountry = models.CharField(max_length = 50)
    addressPostCode = models.CharField(max_length = 10)
    latitiude = models.IntegerField(blank=True, default=0)
    longitude = models.IntegerField(blank=True, default=0)
    phone = models.CharField(max_length = 20)
    website = models.CharField(max_length = 200)
