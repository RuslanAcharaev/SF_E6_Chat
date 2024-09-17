import shortuuid
from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        if self.displayname:
            name = self.displayname
        else:
            name = self.user.username
        return name

    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return static('images/avatar.svg')


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, default=shortuuid.uuid)
    created_at = models.DateField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='chat_groups', blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Message(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.text[:20]}'
