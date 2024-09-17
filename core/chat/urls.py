from django.urls import path
from .views import index_view, profile_view, profile_edit_view, room_view, profiles_list, get_or_create_chatroom, \
    forbidden

urlpatterns = [
    path('', index_view, name='home'),
    path('chat/room/<int:pk>/', room_view, name='room'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit', profile_edit_view, name='profile-edit'),
    path('profiles/', profiles_list, name='profiles'),
    path('chat/<username>', get_or_create_chatroom, name='start-chat'),
    path('forbidden/', forbidden, name='forbidden'),
]
