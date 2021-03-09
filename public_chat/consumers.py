from channels.generic.websocket import AsyncJsonWebSocketConsumer
import json
from django.contrib.auth import get_user_model

User = get_user_model()

class PublicChatConsumer(AsyncJsonWebSocketConsumer):

    async def connect(self):
        """
        Called when the websocket is handshaking as part of the initial connection
        """
        print("PublicChatConsumer: connect: " + str(self.scope['user']))
        await self.accept()

    async def disconnect(self):
        """
        Called when the WebSocket class disconnects
        """
        print("PublicChatConsumer: disconnect ")
        pass

    async def receive_json(self, content):
        """
        Called when we get a text frame. Channels will JSON-decode the payload for us and pass it as the first argument.
        """
        command = content.get("command", None)
        print("PublicChatConsumer: receive_json:  " + str(command))