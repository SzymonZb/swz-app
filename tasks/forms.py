from django.forms import ModelForm

from .models import TaskUpdate

class TaskUpdateForm(ModelForm):
    class Meta:
        model = TaskUpdate
        fields = '__all__'

