from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


class Transmission(models.Model):
    title = models.CharField(max_length=200, default=200,)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, default="Joe")
    body = models.TextField()


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
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('transmission_detail')
    
    

    