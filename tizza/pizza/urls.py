from django.urls import path
from django.views.generic.base import RedirectView
from .views import PizzaView, PizzaRandomView, LikeView, GetTenPizzaView
from pizza.routes import urlpatterns as urlpatterns_pizza_api

urlpatterns = [
    path('<int:id_pizza>/', PizzaView.as_view(), name='pizza-list'),
    path('random/<int:user_id>/', PizzaRandomView.as_view(),
         name='pizza-list-random'),
    path('like/<int:id_pizza>/', LikeView.as_view(), name='pizza-like'),
    path('ten/', GetTenPizzaView.as_view(), name='ten-pizzas'),
]

urlpatterns += urlpatterns_pizza_api
