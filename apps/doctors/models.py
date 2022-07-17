from django.db import models
from ..hospital.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username