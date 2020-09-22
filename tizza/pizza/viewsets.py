from rest_framework import viewsets
from pizza.models import Pizza, Like
from pizza.serializers import PizzaSerializer, LikeSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
