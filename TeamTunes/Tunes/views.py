from django.shortcuts import render

# Create your views here.
from .models import Profile, Event, Song, Album, Genre, Artist, Location
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin

from random import randint


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
        if user.username == 'compsci326':
            continue
        users.append(user)
        num = num + 1

    #get random events

    events = []
    num_events = Event.objects.all().count()
    num = 0
    eventhold = Event.objects.order_by('?')

    for event in eventhold:
        if num >= 6 or num > num_events-1:
            break
        events.append(event)
        num = num + 1


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
    model = Profile




def maps(request):
    """
    For the Map
    """
    #Get List of users
    num_users = User.objects.all().count()
    num = 0
    users = []
    userhold = User.objects.order_by('?')

    for user in userhold:
        if num > num_users-1:
            break
        users.append(user)
        num = num + 1

    #get events

    events = []
    num_events = Event.objects.all().count()
    num = 0
    eventhold = Event.objects.order_by('?')

    for event in eventhold:
        if num > num_events-1:
            break
        events.append(event)
        num = num + 1


    #render HTML
    return render(
    request,
    'maps.html',
    context={"user": users, "event": events}
    )

def my_profile(request):
    logged_in_user = User.objects.get(name = "Tim Richards")
    background_picture = Album.objects.get(name = "Machine Head")
    num_of_events = logged_in_user.events_attended.all().count()
    events_attended = []
    num = 0
    for e_attended in logged_in_user.events_attended.all():
        if num > num_of_events - 1:
            break
        events_attended.append(e_attended)
        num += 1

    num_of_events_attending = logged_in_user.events_attending.all().count()
    num1 = 0
    events_attending = []
    for e in logged_in_user.events_attending.all():
        if num1 > num_of_events_attending - 1:
            break
        num1 += 1
        events_attending.append(e)

    num_of_events_hosting = logged_in_user.events_hosting.all().count()
    num2 = 0
    events_hosting = []
    for e1 in logged_in_user.events_hosting.all():
        if num2 > num_of_events_hosting:
            break
        num2 += 1
        events_hosting.append(e1)

    num_of_followers = logged_in_user.followers.all().count()
    num_of_following = logged_in_user.following.all().count()

    rot = logged_in_user.rotation.all()
    rotate = []
    for i in rot:
        rotate.append(i)

    genres = logged_in_user.favorite_genres.all()
    favorite_genres = []
    for i in genres:
        favorite_genres.append(i)

    songs = logged_in_user.favorite_songs.all()
    favorite_songs = []
    for i in songs:
        favorite_songs.append(i)

    return render(
        request,
        'my_profile.html',
        context={"logged_in_user": logged_in_user, "background_picture": background_picture,
        "events_attended": events_attended, "num_of_following": num_of_following,
        "num_of_followers": num_of_followers, "events_attending": events_attending, "events_hosting": events_hosting,
        "rotate": rotate, "favorite_genres":favorite_genres, "favorite_songs": favorite_songs}
        )

def settings(request):
    logged_in_user = User.objects.get(name = "Tim Richards")
    background_picture = Album.objects.get(name = "Machine Head")
    num_of_followers = logged_in_user.followers.all().count()
    num_of_following = logged_in_user.following.all().count()
    rot = logged_in_user.rotation.all()
    rotate = []
    for i in rot:
        rotate.append(i)

    num_of_events = logged_in_user.events_attended.all().count()
    events_attended = []
    num = 0
    for e_attended in logged_in_user.events_attended.all():
        if num > num_of_events - 1:
            break
        events_attended.append(e_attended)
        num += 1

    num_of_events_attending = logged_in_user.events_attending.all().count()
    num1 = 0
    events_attending = []
    for e in logged_in_user.events_attending.all():
        if num1 > num_of_events_attending - 1:
            break
        num1 += 1
        events_attending.append(e)

    num_of_events_hosting = logged_in_user.events_hosting.all().count()
    num2 = 0
    events_hosting = []
    for e1 in logged_in_user.events_hosting.all():
        if num2 > num_of_events_hosting:
            break
        num2 += 1
        events_hosting.append(e1)

    songs = logged_in_user.favorite_songs.all()
    favorite_songs = []
    for i in songs:
        favorite_songs.append(i)

    return render(
        request,
        'settings.html',
        context={"logged_in_user":logged_in_user, "background_picture": background_picture,
        "num_of_following": num_of_following, "num_of_followers": num_of_followers, "rotate": rotate,
        "events_attending": events_attending, "events_hosting": events_hosting,
        "favorite_songs": favorite_songs,"events_attended": events_attended}
        )

def people(request):

    #Get list of random users
    num_users = User.objects.all().count()
    num = 0
    users = []
    userhold = User.objects.order_by('?')

    for user in userhold:
        if num > num_users-1:
            break
        users.append(user)
        num = num + 1

    #Get songs
    songs = []
    num_songs = Song.objects.all().count()
    num = 0
    songhold = Song.objects.order_by('?')

    for song in songhold:
        if num > num_songs-1:
            break
        songs.append(song)
        num = num + 1

    #render HTML
        return render(
    request,
    'people.html',
    context={"user": users, "song": songs}
    )

#@login_required
#@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
