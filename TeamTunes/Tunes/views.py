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
    hold = User.objects.order_by('?')

    for user in hold:
        if num > 5 or num > num_users-1:
            break
        users.append(user)
        num = num + 1


    events = []

    #Get List of random Events


    #render HTML
    return render(
    request,
    'index.html',
    context={"user": users, "events": events, "num": num_users}
    )

from django.views import generic

class EventDetailView(generic.DetailView):
    model = Event
