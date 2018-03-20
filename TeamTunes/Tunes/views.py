from django.shortcuts import render

# Create your views here.
from .models import Event
from random import randint

from .models import User, Event, Song, Album, Genre, Artist, Location

def index(request):
    """
    For the Home Page
    """
    #Get List of random users
    num_users = User.objects.all().count()
    num = 0
    users = []
    userhold = User.objects.order_by('?')

    for user in userhold:
        if num >= 6 or num > num_users-1:
            break
        users.append(user)
        num = num + 1


    events = []
    num_events = Event.objects.all().count()
    num = 0
    eventhold = Event.objects.order_by('?')

    for event in eventhold:
        if num >= 6 or num > num_events-1:
            break
        events.append(event)
        num = num + 1


    #Get List of random Events


    #render HTML
    return render(
    request,
    'index.html',
    context={"user": users, "event": events}
    )

from django.views import generic

class EventDetailView(generic.DetailView):
    model = Event

class UserDetailView(generic.DetailView):
    model = User
