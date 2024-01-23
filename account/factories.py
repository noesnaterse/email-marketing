import factory
import random
from account.models import Account, User


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    name = factory.Faker("company")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    is_staff = False
    is_active = True
    password = factory.PostGenerationMethodCall("set_password", "password")
