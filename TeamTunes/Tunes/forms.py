class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','bio','anthem','location','email','rotation','profile_picture','hobbies','playlists','latitude','longitude')
