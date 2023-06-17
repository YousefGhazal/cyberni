from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    cv = models.FileField()

    def __str__(self):
        return f"Profile of {self.user.username}"


class Cert(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name
