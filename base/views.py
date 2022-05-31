from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
# Create your views here.

def home(request):
    topics = Topic.objects.all()
    rooms = Room.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)


def roomsView(request, pk):
    rooms2 = Room.objects.get(id=pk)
    participants = rooms2.participants.all() # rooms2 > room ?





    context = {'rooms2': rooms2, 'participants': participants}
    return render(request, 'base/rooms.html', context)


#-------------------------------------------------Create room
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':

        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') #name in the URLs

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

#-------------------------------------------------Update room
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

#-------------------------------------------------Delete room
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/deleteRoom.html', {'obj': room})


