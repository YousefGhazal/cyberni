from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class Gender(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]


class Seeker(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    name = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.PositiveIntegerField(max_length=30)
    email = models.EmailField(unique=True)
    cv = models.FileField()
    link = models.URLField()

    def __str__(self):
        return f"Profile of {self.user.username}"



