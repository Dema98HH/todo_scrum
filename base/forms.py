from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class RoomForm_2(ModelForm):
    class Meta:
        model = Room
        fields = ['participants']
        widgets = {
            'participants': CheckboxSelectMultiple()
        }
        # model = User
        # fields = '__all__'

# class RoomForm(ModelForm):
#     class Meta:
#         model = Room
#         # fields = ['topic', 'name', 'description']
#         fields = ['topic', 'name', 'description']