import random
from django.core.management.base import BaseCommand

from account.factories import AccountFactory, UserFactory


class Command(BaseCommand):
    help = "This command creates some random test data"

    def handle(self, *args, **options):
        for _ in range(random.randrange(2, 5)):
            account = AccountFactory()
            for _ in range(random.randrange(5, 10)):
                user = UserFactory(account=account)
