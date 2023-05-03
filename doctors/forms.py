from django import forms
from .models import Footballer, Profile


class FestivalForm(forms.ModelForm):
    class Meta:
        model = Footballer
        fields = [
            "name",
            "price",
            "age",
        ]


class UploadForm(forms.Form):
    file_upload = forms.FileField()
