from django.urls import re_path, path

from . import consumers
from .models import ChatUser

websocket_urlpatterns = [
    path('ws/chat/<room_name>/', consumers.ChatConsumer.as_asgi()),

]