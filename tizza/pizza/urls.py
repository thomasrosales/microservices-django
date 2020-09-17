from django.urls import path
from django.views.generic.base import RedirectView
from .views import PizzaView, PizzaRandomView

urlpatterns = [
    path('<int:id_pizza>/', PizzaView.as_view(), name='pizza-list'),
    path('random/<int:user_id>', PizzaRandomView.as_view(),
         name='pizza-list-random'),
]
