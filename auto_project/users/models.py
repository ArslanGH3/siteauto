from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    email_verify = models.BooleanField(default=False, verbose_name='Email_verify')

