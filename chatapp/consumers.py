from email import message
import json
from urllib import response
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chatapp.models import *


class ChatConsumer(AsyncWebsocketConsumer):
     async def connect(self):
          self.room_name= f"room_{self.scope['url_route']['kwargs']['room_name']}"
          await self.channel_layer.group_add(self.room_name, self.channel_name) # type: ignore
          await self.accept()
     async def disconnect(self, clode_code): # type: ignore
          await self.channels_layer.group_discard(self.room_name, self.channel_name) # type: ignore


     async def receive(self, text_data): # type: ignore
          text_data_json = json.loads(text_data)

     
     async def send_message(self, event):
          data = event['message']
          await self.create_message(data=data) # type: ignore
          response_data = {
               'sender': data['sender'],
               'message': data['message'],
          }
          await self.send(text_data=json.dumps({'message': response_data}))  


     @database_sync_to_async
     def create_message(self, data):
          get_room_by_name = Room.objects.get(room_name=data['room_name'])
          if not Message.objects.filter(message=data['message']).exists(): # type: ignore