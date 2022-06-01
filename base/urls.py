from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('rooms/<str:pk>/', views.roomsView, name='rooms'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('update-room_2/<str:pk>/part', views.updateRoom_2, name='update-room_2'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
]