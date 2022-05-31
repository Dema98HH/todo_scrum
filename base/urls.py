from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/<str:pk>/', views.roomsView, name='rooms'),
    path('create-room/', views.createRoom, name='create-room'),
]