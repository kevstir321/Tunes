from django.contrib import admin

# Register your models here.
from .models import User, Event, Song, Album, Artist, Genre, Location

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Location)

