from django.shortcuts import render

# Create your views here.
from .models import Event

def index(request):
    """
    For the Home Page
    """
    #Get List of random users

    #Get List of random Events


    #render HTML
    return render(
    request,
    'index.html',
    context={}
    )

from django.views import generic

class EventDetailView(generic.DetailView):
    model = Event
