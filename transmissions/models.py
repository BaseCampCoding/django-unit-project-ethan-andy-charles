from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from accounts.models import CustomUser
from django_userforeignkey.models.fields import UserForeignKey

class Transmission(models.Model):
    title = models.CharField(max_length=200, default=200,)
    author = UserForeignKey(
        auto_user_add=True,
        verbose_name="User is automatically assigned",
        related_name="Tranmission.author+",
    )
    body = models.TextField()
    likes = models.ManyToManyField(CustomUser, related_name='transmission_like')


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('transmission_detail', args=[str(self.id)])

class Comment(models.Model):
    transmission = models.ForeignKey(
        Transmission, 
        on_delete=models.CASCADE,
        related_name='comments',
        )
    comment = models.CharField(max_length=140)
    author = UserForeignKey(
        auto_user_add=True,
        verbose_name="User is automatically assigned",
        related_name="joe",
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse_lazy('transmission_detail', args=[str(self.transmission.id)])

    