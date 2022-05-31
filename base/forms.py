from django.forms import ModelForm
from .models import Room

# class RoomForm(ModelForm):
#     class Meta:
#         model = Room
#         fields = '__all__'

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # fields = ['topic', 'name', 'description']
        fields = ['topic', 'name', 'description']