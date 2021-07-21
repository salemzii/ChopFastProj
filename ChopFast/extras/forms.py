from django import forms
from .models import Tasks


class AddTask(forms.ModelForm):

    class Meta:
        fields = ['title', 'task']
        model = Tasks


class TaskUpdateForm(forms.ModelForm):

    class Meta:
        fields = ['title', 'task']
        model = Tasks
        
