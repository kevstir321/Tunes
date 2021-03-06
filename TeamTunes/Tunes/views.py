from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import Profile, Event, Song, Album, Genre, Artist, Location
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin

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

from .forms import Add_Friend_Form, Add_Event_Form

class EventDetailView(FormMixin,generic.DetailView):
    model = Event
    form_class = Add_Event_Form

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['form'] = Add_Event_Form(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        logged_in_user = request.user.profile
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            logged_in_user.events_attending.add(Event.objects.get(id=self.kwargs['pk']))
            logged_in_user.save()
            other = Event.objects.get(id=self.kwargs['pk'])
            other.people.add(logged_in_user)
            other.save()
            return redirect(request.path_info)
        else:
            return self.form_invalid(form)


class UserDetailView(FormMixin,generic.DetailView):
    model = Profile
    form_class = Add_Friend_Form

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['form'] = Add_Friend_Form(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        logged_in_user = request.user.profile
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            logged_in_user.following.add(Profile.objects.get(id=self.kwargs['pk']))
            logged_in_user.save()
            other = Profile.objects.get(id=self.kwargs['pk'])
            other.followers.add(logged_in_user)
            other.save()
            return redirect(request.path_info)
        else:
            return self.form_invalid(form)




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
        if num >= 6 or num > num_users-1:
            break
        if user.username == 'compsci326':
            continue
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
from django.db import transaction

@login_required
@transaction.atomic
def update_profile(request):
    logged_in_user = request.user.profile
    num_of_followers = logged_in_user.followers.all().count()
    num_of_following = logged_in_user.following.all().count()
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

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST,request.FILES)
        profile_picture_form = Profile_Picture_Form(request.POST)
        profile_rotation = RotationForm(request.POST)
        profile_favorite_songs = Favorite_Songs_Form(request.POST)
        profile_favorite_genres = Favorite_Genres_Form(request.POST)
        profile_current_song = Current_Song_Form(request.POST)
        i = 0

        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.set_password(user_form.cleaned_data.get('password'))
            user.save()
            i = 1
            #return redirect('settings')
        else:
            pass

        if profile_form.is_valid():
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            profile_form.full_clean()
            profile_form.save()
            i = 1
            #return redirect('settings')
        else:
            pass

        if profile_rotation.is_valid():
            profile_rotation = RotationForm(request.POST, instance=request.user.profile)
            profile_rotation.save()
            #return redirect('settings')
            i = 1
        else:
            pass

        if profile_favorite_songs.is_valid():
            profile_favorite_songs = Favorite_Songs_Form(request.POST, instance=request.user.profile)
            profile_favorite_songs.save()
            #return redirect('settings')
            i = 1
        else:
            pass

        if profile_favorite_genres.is_valid():
            profile_favorite_genres = Favorite_Genres_Form(request.POST, instance=request.user.profile)
            profile_favorite_genres.save()
            i = 1
            #return redirect('settings')
        else:
            pass

        if profile_current_song.is_valid():
            profile_current_song = Current_Song_Form(request.POST, instance=request.user.profile)
            profile_current_song.save()
            i = 1
            #return redirect('settings')
        else:
            pass

        if i == 1:
            return redirect('settings')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        profile_favorite_songs = Favorite_Songs_Form(instance=request.user.profile)
        profile_favorite_genres = Favorite_Genres_Form(instance=request.user.profile)
        profile_current_song = Current_Song_Form(instance=request.user.profile)
        profile_rotation = RotationForm(instance=request.user.profile)

    return render(request, 'settings.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'num_of_followers': num_of_followers,
        'num_of_following': num_of_following,
        'logged_in_user': logged_in_user,
        'background_picture': background_picture,
        'profile_rotation': profile_rotation,
        'profile_favorite_songs': profile_favorite_songs,
        'profile_favorite_genres': profile_favorite_genres,
        'profile_current_song': profile_current_song,
        'events_attended': events_attended,
        'events_attending': events_attending,
        'events_hosting': events_hosting,
        'favorite_genres': favorite_genres,
        'favorite_songs': favorite_songs,
        'rotate': rotate
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
        if user.username == 'compsci326':
            continue
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
    success_url = reverse_lazy('index')

from .forms import UserForm, ProfileForm
from django.db import transaction

#@login_required
@transaction.atomic
def create_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.set_password(user_form.cleaned_data.get('password'))
            user.save()
            profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
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
