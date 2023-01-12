import datetime
import re
from django import forms
from .models import Album, Photo
from django.forms import ModelForm


class AlbumForm(forms.ModelForm):
    album_name = forms.CharField(
        error_messages={'required': 'Please enter Album name'},
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Album Name",
            "class": "form-control",
        }))
    private = forms.BooleanField(
        required=False
    )

    class Meta:
        model = Album
        fields = [
            'album_name',
            # 'user',
            'private',
        ]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'title',
            'private',
            'album_cover',
            'photo'
        ]
