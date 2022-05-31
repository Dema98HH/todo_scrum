from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name=''),
    path('rooms/<str:pk>/', views.roomsView, name='rooms'),
]