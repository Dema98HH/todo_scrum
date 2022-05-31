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
    context = {'rooms2': rooms2}
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


