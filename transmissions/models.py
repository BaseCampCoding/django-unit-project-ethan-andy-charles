from django.db import models


class Transmission(models.Model):
    title = models.CharField(max_length=200, default=200,)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, default="Joe")
    body = models.TextField()


    def __str__(self):
        return self.title