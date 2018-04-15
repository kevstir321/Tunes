"""
TODO
"""

from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','bio','anthem','location','email','rotation','profile_picture','hobbies','playlists','latitude','longitude')
