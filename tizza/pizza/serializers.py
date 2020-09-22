from pizza.models import Pizza, Like
from rest_framework import serializers
from user.serializers import UserProfileSerializer


class PizzaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pizza
        fields = ('id', 'title', 'description')


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    user = UserProfileSerializer()
    pizza = PizzaSerializer()

    class Meta:
        model = Like
        fields = ('id', 'user', 'pizza')
