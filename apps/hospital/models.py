from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False) 