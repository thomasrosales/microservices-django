from django.core.management.base import BaseCommand, CommandError
import json
from pizza.models import Like
from pizza.utils.consumer import consumer
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Consumes user deleted messages from RabbbitMQ"

    def callback(channel, method, properties, body):
        payload = json.loads(body)
        user_id = payload.get('user_id')
        if user_id is not None:
            likes = Like.objects.filter(user__id=user_id)
            logger.error(f'Like({likes})')
            likes.delete()

    def handle(self, *args, **kwargs):
        logger.error(' [*] Waiting for logs. To exit press CTRL+C')
        consumer.consume(exchange='users', queue_name='users-deleted',
                         routing_key='user.deleted', callback=self.callback)
