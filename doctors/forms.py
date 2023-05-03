from django import forms
from .models import Footballer, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FestivalForm(forms.ModelForm):
    class Meta:
        model = Footballer
        fields = [
            "name",
            "price",
            "age",
        ]


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
