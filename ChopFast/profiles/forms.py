from django import forms
from .models import Customer, Rider, Staff, Supplier


class CustomerUpdateForm(forms.ModelForm):
    address = forms.CharField(
                widget=forms.TextInput(
                attrs={
                "placeholder" : "Address",                
                "class": "form-control"
            }
    ))
    image = forms.ImageField()
    class Meta:
        model = Customer
        fields = [ 'address','image']


class RiderUpdateForm(forms.ModelForm):
    address = forms.CharField(
                widget=forms.TextInput(
                attrs={
                "placeholder" : "Address",                
                "class": "form-control"
            }
    ))
    image = forms.ImageField()
    class Meta:
        model = Rider
        fields = [ 'address','image']


class StaffUpdateForm(forms.ModelForm):
    address = forms.CharField(
                widget=forms.TextInput(
                attrs={
                "placeholder" : "Address",                
                "class": "form-control"
            }
    ))
    image = forms.ImageField()
    class Meta:
        model = Staff
        fields = [ 'address','image']

