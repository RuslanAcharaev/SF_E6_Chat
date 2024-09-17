from chat.models import Profile, Room, Message
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = ['user_id', 'username', 'image', 'displayname', 'info']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['name', 'created_at', 'is_private', 'members']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['author', 'text', 'room', 'created_at']
