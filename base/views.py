from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .models import Room, Topic, Task, User
from .forms import RoomForm, RoomForm_2, TaskForm
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.


def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username') # .lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
     page = 'register'

     form = UserCreationForm()

     if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save(commit=False)
             user.username = user.username # .lower()
             user.save()
             login(request, user)
             return redirect('home')
         else:
            messages.error(request, 'An error occurred during registration')
     return render(request, 'base/login_register.html', {'form': form})


def userInfo(request, pk):
    userinfo = User.objects.get(id=pk)
    context = {'userinfo': userinfo}

    return render(request, 'base/userInf.html', context)









def home(request):

    form = RoomForm()
    data = Task.objects.all()
    if request.method == 'POST':

        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') #name in the URLs

    # context = {'form': form}

    topics = Topic.objects.all()
    rooms = Room.objects.all()
    context = {'rooms': rooms, 'topics': topics, 'form': form, 'data': data}
    return render(request, 'base/home.html', context)


def roomsView(request, rom_id):
    rooms2 = Room.objects.get(id=rom_id)
    tasks = Task.objects.filter(hostroom_id=rom_id)
    participants = rooms2.participants.all() # rooms2 > room ?

    form = TaskForm()

    if request.method == 'POST':

        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            return JsonResponse({'task': model_to_dict(new_task)}, status=200)



    context = {'rooms2': rooms2, 'participants': participants, 'tasks': tasks, 'form':form}
    return render(request, 'base/rooms.html', context)





# class TaskComplete(View):
def postTask(request, pk):

    task = Task.objects.get(id=pk)
    task.finish = True
    task.save()
    return JsonResponse({'task': model_to_dict(task)}, status=200)
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




def updateRoom_2(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm_2(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        form = RoomForm_2(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms', room.pk)

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

# test

# def Delete(request, id=None):
#     Task.objects.get(id=id).delete()
#     return redirect('home')
#
# def Complete(request, id=None):
#     data = Task.objects.get(id=id)
#     data.finish = True
#     data.save()
#
#     return redirect('home')
#
# def InComplete(request, id=None):
#     data = Task.objects.get(id=id)
#     data.complete = False
#     data.save()
#     return redirect('home')
