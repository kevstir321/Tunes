from django.contrib import admin

# Register your models here.
from .models import User, Event, Song

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Song)
