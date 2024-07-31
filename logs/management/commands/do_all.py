from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = "Starts all consumers for RabbitMQ"

    def handle(self, *args, **options):
        call_command('get_all_todos', *args, **options)