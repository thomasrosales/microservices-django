from django.urls import path
from django.views.generic.base import RedirectView
from .views import PizzaView

urlpatterns = [
    path('<int:id_pizza>/', PizzaView.as_view(), name='pizza-list'),
]
