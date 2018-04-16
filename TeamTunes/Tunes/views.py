from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import Profile, Event, Song, Album, Genre, Artist, Location
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
    curr_user = request.user
    follow = curr_user.profile.followers.all()

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

@login_required
def my_profile(request):
    logged_in_user = request.user.profile
    background_picture = Album.objects.get(name = "Soul")
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

from .forms import UserForm, ProfileForm, Profile_Picture_Form, RotationForm, Favorite_Songs_Form, Favorite_Genres_Form, Current_Song_Form

@login_required
#@transaction.atomic
def update_profile(request):
    logged_in_user = request.user.profile
    num_of_followers = logged_in_user.followers.all().count()
    num_of_following = logged_in_user.following.all().count()
    background_picture = Album.objects.get(name = "Soul")
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        profile_picture_form = Profile_Picture_Form(request.POST, instance=request.user.profile)
        profile_rotation = RotationForm(request.POST, instance=request.user.profile)
        profile_favorite_songs = Favorite_Songs_Form(request.POST, instance=request.user.profile)
        profile_favorite_genres = Favorite_Genres_Form(request.POST, instance=request.user.profile)
        profile_current_song = Current_Song_Form(request.POST, instance=request.user.profile)

        if (profile_picture_form.is_valid() and user_form.is_valid() and
        profile_form.is_valid() and profile_rotation.is_valid() and
        profile_favorite_songs.is_valid() and profile_favorite_genres.is_valid() and profile_current_song.is_valid()):
            user_form.save()
            profile_form.save()
            profile_picture_form.save()
            profile_favorite_songs.save()
            profile_favorite_genres.save()
            profile_current_song.save()
            profile_rotation.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            pass
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        profile_picture_form = Profile_Picture_Form(instance=request.user.profile)
        profile_favorite_songs = Favorite_Songs_Form(instance=request.user.profile)
        profile_favorite_genres = Favorite_Genres_Form(instance=request.user.profile)
        profile_current_song = Current_Song_Form(instance=request.user.profile)
        profile_rotation = RotationForm(instance=request.user.profile)

    return render(request, 'settings.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile_picture_form': profile_picture_form,
        'num_of_followers': num_of_followers,
        'num_of_following': num_of_following,
        'logged_in_user': logged_in_user,
        'background_picture': background_picture,
        'profile_rotation': profile_rotation,
        'profile_favorite_songs': profile_favorite_songs,
        'profile_favorite_genres': profile_favorite_genres,
        'profile_current_song': profile_current_song
    })

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

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class EventCreate(CreateView):
    model = Event
    fields = '__all__'

class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'
class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('')

from .forms import UserForm, ProfileForm
from django.db import transaction

#@login_required
@transaction.atomic
def create_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.set_password(user_form.cleaned_data.get('password'))
            user.save()
            profile_form = ProfileForm(request.POST, instance=user.profile)
            profile_form.full_clean()
            profile_form.save()
            return redirect('login')
        else:
            pass
            #messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
    return render(request, 'create_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
