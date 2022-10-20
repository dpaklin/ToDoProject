from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class TodoUser(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    