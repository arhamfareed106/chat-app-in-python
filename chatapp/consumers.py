from email import message
import json
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


     async def receive(self, text_data) : # type: ignore
          test_data_json = json.loads(text_data)
          message= text_data_json