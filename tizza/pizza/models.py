from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile


# Create your models here.


class Pizzeria(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return f'Pizzeria({self.id}, {self.owner.id})'

    def to_json(self):
        json = dict()
        json['id'] = self.id
        json['owner'] = self.owner
        json['address'] = self.address
        json['phone'] = self.phone
        return json


class Pizza(models.Model):
    MEAT = 'MEA'
    VEGETARIAN = 'VEGE'
    VEGAN = 'VEGA'
    NONE = 'None'
    KIND_PIZZA_CHOICES = [
        (MEAT, 'Meat'),
        (VEGETARIAN, 'Vegetarian'),
        (VEGAN, 'Vegan'),
        (NONE, '')
    ]

    title = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField()
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, on_delete=models.CASCADE)
    kin_of_pizza = models.CharField(
        max_length=4,
        choices=KIND_PIZZA_CHOICES,
        default=NONE
    )

    def __str__(self):
        return f'Pizza({self.id}, {self.title})'

    def to_json(self):
        json = dict()
        json['id'] = self.id
        json['title'] = self.title
        json['description'] = self.description
        json['thumbnail_url'] = self.thumbnail_url
        json['approved'] = self.approved
        json['creator'] = self.creator.to_json()
        return json


class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'pizza',)

    def __str__(self):
        return f'Like({self.id}, User({self.user.id}), Pizza({self.pizza.id}))'

    def to_json(self):
        json = dict()
        json['id'] = self.id
        json['user'] = self.user.id
        json['pizza'] = self.pizza.to_json()
        return json
