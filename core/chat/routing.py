from django.urls import path, re_path
from .consumers import WSConsumer


ws_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', WSConsumer.as_asgi())
]
