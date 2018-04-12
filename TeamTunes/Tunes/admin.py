from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Profile, Event, Song, Album, Artist, Genre, Location, Playlist

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Location)
admin.site.register(Playlist)
