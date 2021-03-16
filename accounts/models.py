from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy, reverse
# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('user_profile', args=[str(self.id)])