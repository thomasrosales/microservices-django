from django.urls import path, include
from user.viewsets import UsersViewSet

user_detail = UsersViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('api/v1/user/<int:pk>/', user_detail, name='user-detail'),
]
