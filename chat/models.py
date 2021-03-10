from django.db import models
from django.conf import settings

# Create your models here.
class ChatUser(models.Model):
    """
    Chat message created by a user inside a PublicChatRoom
    """
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp           = models.DateTimeField(auto_now_add=True)
    message            = models.TextField(unique=False, blank=False,)

    def __str__(self):
        return self.content
