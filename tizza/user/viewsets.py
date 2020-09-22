from rest_framework import viewsets
from user.serializers import UserSerializer
from user.models import User
from pizza.utils.producer import producer
from rest_framework.decorators import action


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, pk, *args, **kwargs):
        user = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        producer.produce(exchange='user', body={
                         'user_id': user.id}, routing_key='user.deleted')
        return response
