from django.urls import path, include
from django.views.generic.base import RedirectView
from user.views import SignupView
from django.contrib.auth import urls as auth_urls
from user.routes import urlpatterns as urlpatterns_user_api

urlpatterns = [
    path('', include(auth_urls)),
    path('register/', SignupView.as_view(), name='sign-up'),
]


urlpatterns += urlpatterns_user_api
