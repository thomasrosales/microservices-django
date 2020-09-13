from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Pizza


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
