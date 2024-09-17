from django.urls import re_path
from .consumers import WSConsumer


ws_urlpatterns = [
    re_path(r'^ws/chat/room/(?P<room_name>\d+)/', WSConsumer.as_asgi())
]
