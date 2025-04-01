from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.get_full_name() if self.get_full_name() else self.username
