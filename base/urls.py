from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/<str:pk>/', views.roomsView, name='rooms'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
]