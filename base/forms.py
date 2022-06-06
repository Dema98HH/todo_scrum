from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Room, User, Task

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


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

# class TasksForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['finish']
#         widgets = {
#             'finish': CheckboxSelectMultiple()
#         }
# class RoomForm(ModelForm):
#     class Meta:
#         model = Room
#         # fields = ['topic', 'name', 'description']
#         fields = ['topic', 'name', 'description']