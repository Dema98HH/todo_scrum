import crispy_forms
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django import forms
# from models import *
# from django.forms import *
from django.urls import reverse

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
# Create your models here.



class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants')
    updated = models.DateTimeField(auto_now=True)
    createed = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-createed']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('roomm', kwargs={'rom_id': self.pk})


class Task(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hostroom = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    finish = models.BooleanField(default=False)

    def __str__(self):
        return self.name


