from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Task

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Task)

