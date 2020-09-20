from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Pizza, Like
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ratelimit.decorators import ratelimit
from user.models import UserProfile

import random


# Create your views here.

@method_decorator(ratelimit(key='ip', rate='5/m', method='GET', block=True), name='get')
class PizzaView(View):

    @method_decorator(login_required)
    def get(self, request, id_pizza, *args, **kwargs):
        try:
            pizza = Pizza.objects.get(id=id_pizza)
            return HttpResponse(content=pizza.to_json().values(), status=200)
        except Pizza.DoesNotExist:
            response = {'status': "error", 'message': 'pizza not found'}
            html = f'<html><body>{response}</body></html>'
            return HttpResponse(html, status=403)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        new_pizza = Pizza.objects.create(
            title=data['title'], description=data['description'], creator=request.user)
        new_pizza.save()
        return HttpResponse(content=pizza.to_json(), status=201)


class GetTenPizzaView(View):
    template_name = 'ten_pizzas.html'

    def get(self, request):
        pizzas = Pizza.objects.order_by('id')[:10]
        return render(request, self.template_name, {'pizzas': pizzas})


class PizzaRandomView(View):

    @method_decorator(login_required)
    def get(self, request, user_id, *args, **kwargs):
        try:
            likes = [l.pizza.id for l in Like.objects.filter(user__id=user_id)]
            pizzas = Pizza.objects.all().exclude(id__in=likes)
            pre_selected_pizzas = list()
            for p in pizzas:
                pre_selected_pizzas.append(p.title)
            if len(pizzas) >= 15:
                choosier_pizzas = random.sample(pre_selected_pizzas, 15)
            return HttpResponse(choosier_pizzas, status=200)
        except Pizza.DoesNotExist:
            response = {'status': "error", 'message': 'pizza not found'}
            html = f'<html><body>{response}</body></html>'
            return HttpResponse(html, status=403)


class LikeView(View):

    @method_decorator(login_required)
    def post(self, request, id_pizza, *args, **kwargs):
        try:
            user = UserProfile.objects.get(user=request.user)
            pizza = Pizza.objects.get(id=id_pizza)
            like = Like(user=user, pizza=pizza)
            like.save()
            return HttpResponse(status=201)
        except (Pizza.DoesNotExist, UserProfile.DoesNotExist) as e:
            response = {'status': "error", 'message': e}
            html = f'<html><body>{response}</body></html>'
            return HttpResponse(html, status=403)

    @method_decorator(login_required)
    def delete(self, request, id_pizza, *args, **kwargs):
        try:
            like = Like.objects.get(user=request.user, pizza__id=id_pizza)
            like.delete()
            return HttpResponse(status=200)
        except Pizza.DoesNotExist as e:
            response = {'status': "error", 'message': e}
            html = f'<html><body>{response}</body></html>'
            return HttpResponse(html, status=403)
