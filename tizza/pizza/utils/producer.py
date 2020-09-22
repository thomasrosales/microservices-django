import json
import pika
import sys
from django.conf import settings
import os


class Producer:
    connection = None
    channel = None
    exchanges = None

    def __init__(self, host, username, password):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(f'amqp://{username}:{password}@{host}:5672'))
        self.channel = self.connection.channel()
        self.exchanges = []

    def produce(self, exchange, body, routing_key=''):
        if exchange not in self.exchanges:
            self.channel.exchange_declare(exchange=exchange)
            self.exchanges.append(exchange)
            self.channel.basic_publish(
                exchange=exchange, routing_key=routing_key, body=json.dumps(body))
            print(" [x] Sent %r:%r" % ('payload', body))


producer = Producer(
    host=os.environ.get('RABBITMQ_HOST', 'localhost'),
    username=os.environ.get('RABBITMQ_USERNAME', 'guest'),
    password=os.environ.get('RABBITMQ_PASSWORD', 'guest')
)
