from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete users'

    def add_arguments(self, parser):
        parser.add_argument('number_user', nargs='+', type=int)

    def handle(self, *args, **options):
        User = get_user_model()
        users = options['number_user']
        superuser = User.objects.filter(is_superuser=True, id__in=users).exists()
        if superuser:
            raise Exception('This user cannot be deleted')
        fil_user = User.objects.filter(id__in=users)
        fil_user.delete()
