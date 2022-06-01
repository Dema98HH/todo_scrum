from django.forms import ModelForm
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class RoomForm_2(ModelForm):
    class Meta:
        model = Room
        fields = ['participants']
        # model = User
        # fields = '__all__'

# class RoomForm(ModelForm):
#     class Meta:
#         model = Room
#         # fields = ['topic', 'name', 'description']
#         fields = ['topic', 'name', 'description']