from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Prints Greetings message'

    def add_arguments(self, parser):
        # The only change is here: add dashes to the argument name.
        parser.add_argument(
            '--name',
            type=str,
            help='Name to greet',
            default='World' # Default is used if the --name flag is not provided
        )

    def handle(self, *args, **kwargs):
        # The rest of the code works perfectly!
        name = kwargs['name']
        self.stdout.write(self.style.SUCCESS(f'Hi {name}, Greetings from Django Management Command!'))