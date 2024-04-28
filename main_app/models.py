from django.db import models
from user.models import User

class Practice(models.Model):
    dietitian = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length = 150)
    address = models.CharField(max_length = 250)
    latitiude = models.IntegerField(blank=True, default=0)
    longitude = models.IntegerField(blank=True, default=0)
    phone = models.CharField(max_length = 20)
    website = models.CharField(max_length = 200)
