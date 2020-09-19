from django.urls import path, include
from django.views.generic.base import RedirectView
from .views import SignupView
from django.contrib.auth import urls as auth_urls


urlpatterns = [
    path('', include(auth_urls)),
    path('register/', SignupView.as_view(), name='sign-up'),

]
