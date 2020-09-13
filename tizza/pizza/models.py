from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile


# Create your models here.


class Pizzeria(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)


class Pizza(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField()
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, on_delete=models.CASCADE)


class LikeS(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
