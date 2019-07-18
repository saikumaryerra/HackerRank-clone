from django.urls import path
from main import consumers

websocket_urlpatterns = [
    path('interview/<room_name>', consumers.ChatConsumer),
]