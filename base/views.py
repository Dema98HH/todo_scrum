from django.shortcuts import render, redirect
from .models import Room, Topic
# Create your views here.

def home(request):
    topics = Topic.objects.all()
    rooms = Room.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)


def roomsView(request, pk):
    rooms2 = Room.objects.get(id=pk)
    context = {'rooms2': rooms2}
    return render(request, 'base/rooms.html', context)

