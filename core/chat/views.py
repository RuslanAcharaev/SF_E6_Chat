from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect, reverse

from .forms import ProfileForm
from .models import Room, Message, Profile


def index_view(request):
    if not request.user.is_authenticated:
        return redirect('forbidden')
    if request.method == 'POST':
        room_name = request.POST.get('room_name', None)
        if room_name:
            if Room.objects.filter(name=room_name).exists():
                room = Room.objects.get(name=room_name)
                return HttpResponseRedirect(reverse('room', args=[room.pk]))
            else:
                room = Room.objects.create(name=room_name)
                return HttpResponseRedirect(reverse('room', args=[room.pk]))

    rooms_list = Room.objects.all()
    context = {'rooms': rooms_list}
    return render(request, 'home.html', context)


def room_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('forbidden')
    room: Room = get_object_or_404(Room, pk=pk)
    messages = Message.objects.filter(room=room)

    other_user = None
    if room.is_private:
        if request.user not in room.members.all():
            raise Http404()
        for member in room.members.all():
            if member != request.user:
                other_user = member
                break

    context = {
        'room': room,
        'messages': messages,
        'other_user': other_user,
    }

    return render(request, 'room.html', context)


def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect('account_login')
    return render(request, 'users/profile.html', {'profile': profile})


@login_required()
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'users/profile_edit.html', {'form': form})


def profiles_list(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles.html', context)


@login_required()
def get_or_create_chatroom(request, username):
    if request.user.username == username:
        return redirect('home')

    other_user = User.objects.get(username=username)
    private_rooms = Room.objects.filter(is_private=True)

    if private_rooms.exists():
        for chatroom in private_rooms:
            if (other_user in chatroom.members.all()) and (request.user in chatroom.members.all()):
                room = chatroom
                break
        if 'room' not in locals():
            room = Room.objects.create(is_private=True)
            room.members.add(other_user, request.user)
    else:
        room = Room.objects.create(is_private=True)
        room.members.add(other_user, request.user)

    pk = room.pk

    return redirect('room', pk)


def forbidden(request):
    return render(request, 'forbidden.html')
