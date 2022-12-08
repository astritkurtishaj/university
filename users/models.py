from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    departments = models.ManyToManyField('departments.Department')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @staticmethod
    def create_user(email, password, **extra_fields):
        user = User(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


