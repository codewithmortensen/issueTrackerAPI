from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class User(AbstractUser):
    first_name = models.CharField(
        max_length=50, validators=[MinLengthValidator(3, message='Please provide a valid first name')])
    last_name = models.CharField(
        max_length=50, validators=[MinLengthValidator(3, message='Please provide a valid last name')])
    email = models.EmailField(unique=True, max_length=50)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
