import json
import os

from django.core.management.base import BaseCommand, CommandError
from core.models import FastConsumer
from logs.models import Log

class Command(BaseCommand):
    help = "Consumes get all todos messages from RabbitMQ"

    def handle(self, *args, **options):
        consumer = FastConsumer(
            callback=self._callback,
            name='todos',
            exchange=os.getenv('TODOS_EXCHANGE'),
            routing_key=os.getenv('TODOS_ALL_ROUTING_KEY')
        )

        consumer.consume(auto_ack=True)

        print('Consumer shutting down...')

    def _callback(self, channel, method, properties, body):
        message = json.loads(body)
        print(f" [x] Received {message}")
        log = Log(message=message, level='I')
        log.save()
        print(" [x] Done")