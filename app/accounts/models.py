import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    # email = models.EmailField("email address", blank=True, unique=True)
    # username = models.CharField('username', max_length=150, unique=True, default=str(uuid.uuid4()))
#