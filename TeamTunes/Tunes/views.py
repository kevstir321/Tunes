from django.shortcuts import render

# Create your views here.

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
