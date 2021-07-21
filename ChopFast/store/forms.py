from django import forms
from .models import Dish


class AddDish(forms.ModelForm):

    class Meta:
        model = Dish 
        fields = ['name', 'description', 'image', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'description'})
        }


class EditDish(forms.ModelForm):

    class Meta:
        model = Dish 
        fields = ['name', 'description', 'image', 'price', 'available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'description'})
        }