from django.urls import path
from .views import index_view, profile_view, profile_edit_view, room_view

urlpatterns = [
    path('', index_view, name='home'),
    path('chat/<str:room_name>/', room_view, name='room'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit', profile_edit_view, name='profile-edit')
]
