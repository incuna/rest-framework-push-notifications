import factory
from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence('User {}'.format)

    class Meta:
        model = User
