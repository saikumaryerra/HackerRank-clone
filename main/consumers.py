from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Room , RoomMember

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        try:
            room = Room.objects.filter(roomname = self.room_group_name)[0]
            if room.users < 2:
                async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
                )

                roommember = RoomMember.objects.create(room = room)
                roommember.name = self.channel_name
                roommember.save()

                room.users= room.users+1
                room.save()
                self.accept()                
                self.send(text_data=json.dumps({
                'type' : 'video_start',
                'message': 'not initiator'
                }))
        except:
            room = Room.objects.create()
            async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
            )
            room.roomname = self.room_group_name
            room.users = 1
            roommember = RoomMember.objects.create(room = room)
            roommember.name = self.channel_name
            roommember.save()
            # room.rand = a;
            room.save()
            self.accept()

            self.send(text_data=json.dumps({
            'type' : 'video_start',
            'message': 'initiator'
            }))

        # Join room group
        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        # room = Room.objects.filter(roomname = self.room_group_name)[0]
        # if room.users > 1:
        #     room.users = room.users-1
        #     room.save()
        # else :
        #     room.delete()
                
        # roommember = RoomMember.objects.filter(room = room ,name = self.channel_name)[0]
        # roommember.delete()
        
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
        


    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type = text_data_json['type']
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': type,
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        type = event['type']
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type1' : type,
            'message': message
        }))
    
    def code_message(self, event):
        type = event['type']
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type1' : type,
            'message': message
        }))
    def output_message(self, event):
        type = event['type']
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type1' : type,
            'message': message
        }))
