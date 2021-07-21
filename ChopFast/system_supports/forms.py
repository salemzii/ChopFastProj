from django import forms
from .models import Feedback, reportRestaurant


class Create_feedback(forms.ModelForm):
    class Meta:
        fields = ['title', 'feedback']
        model = Feedback


class reportRestaurantForm(forms.ModelForm):
    class Meta:
        model = reportRestaurant
        fields = ['report']