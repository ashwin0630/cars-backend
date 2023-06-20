from django import forms
from django.forms import ModelForm
from .models import car_details

class carform(ModelForm):
    class Meta:
        model=car_details
        fields='__all__'
        widgets = {
            'year_of_registration': forms.DateInput(attrs={'type': 'date'}),
        }


        