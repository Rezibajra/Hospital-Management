from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    name = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
    )

    def __str__(self):
        return self.name