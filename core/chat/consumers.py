import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from .models import Room, Profile, Message


class WSConsumer(AsyncWebsocketConsumer):
    # Установка соединения
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    # Разрыв соединения
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Получение сообщения от WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        await self.create_message(data=text_data_json)

        event = {
            'type': 'send_message',
            'message': text_data_json
        }

        await self.channel_layer.group_send(self.room_group_name, event)

    # Отправка сообщения на WebSocket
    async def send_message(self, event):
        data = event['message']

        response = {
            'author': data['author'],
            'message': data['message'],
            'avatar': data['avatar']
        }

        await self.send(text_data=json.dumps({'message': response}))

    # Создание экземпляра сообщения в БД
    @database_sync_to_async
    def create_message(self, data):
        get_room = Room.objects.get(name=data['room'])
        get_username = User.objects.get(username=data['author'])
        get_user = Profile.objects.get(user=get_username)

        new_message = Message.objects.create(
            author=get_user,
            text=data['message'],
            room=get_room
        )


