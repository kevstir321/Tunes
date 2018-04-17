"""
TODO
"""

from django import forms
from .models import Profile
from .models import Event
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','first_name','last_name')

class RotationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("rotation",)

class Favorite_Songs_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("favorite_songs",)

class Favorite_Genres_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("favorite_genres",)

class Current_Song_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("current_song",)

class Profile_Picture_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','bio','anthem','location','email', 'hobbies','playlists','latitude','longitude')

class Add_Friend_Form(forms.Form):
    pass
