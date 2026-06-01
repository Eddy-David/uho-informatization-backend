from django.urls import re_path
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send_json({'message': 'Conectado al canal de notificaciones UHO'})

    async def receive_json(self, content):
        await self.send_json({'message': 'Datos recibidos', 'content': content})


websocket_urlpatterns = [
    re_path(r'ws/notifications/$', NotificationConsumer.as_asgi()),
]
