from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Pizza, Like

import random


# Create your views here.


class PizzaView(View):

    def get(self, request, *args, **kwargs):
        try:
            pizza = Pizza.objects.get(id=kwargs['id_pizza'])
            return HttpResponse({'id': pizza.id, 'title': pizza.title, 'description': pizza.description})
        except Pizza.DoesNotExist:
            response = {'status': "error", 'message': 'pizza not found'}
            html = f'<html><body>{response}</body></html>'
            return HttpResponse(html, status=403)


class PizzaRandomView(View):

    def get(self, request, user_id, *args, **kwargs):
        try:
            likes = [l.pizza.id for l in Like.objects.filter(user__id=user_id)]
            pizzas = Pizza.objects.all().exclude(id__in=likes)
            pre_selected_pizzas = list()
            for p in pizzas:
                pre_selected_pizzas.append(p.title)
            if len(pizzas) >= 15:
                choosier_pizzas = random.sample(pre_selected_pizzas, 15)
                print(choosier_pizzas)
            return HttpResponse()
        except Pizza.DoesNotExist:
            response = {'status': "error", 'message': 'pizza not found'}
            html = f'<html><body>{response}</body></html>'
            return HttpResponse(html, status=403)
