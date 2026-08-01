from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=50, unique=True,
                                    blank=True, null=True)  #WARNING: for now null

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
