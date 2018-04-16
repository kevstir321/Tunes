from django.urls import path
from django.urls import re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^user/(?P<pk>[-\w]+)$', views.UserDetailView.as_view(), name='user-detail'),
    re_path(r'^event/(?P<pk>[-\w]+)$', views.EventDetailView.as_view(), name='event-detail'),
    path('maps.html', views.maps, name='maps'),
    path('my_profile.html', views.my_profile, name = "my_profile"),
    path('settings.html', views.update_profile, name = "settings"),
    path('people.html', views.people, name='people'),
]


urlpatterns += [
    path('event/create/', views.EventCreate.as_view(), name='event_create'),
    re_path(r'^event/(?P<pk>[-\w]+)/update/$', views.EventUpdate.as_view(), name='event_update'),
    re_path(r'^event/(?P<pk>[-\w]+)/delete/$', views.EventDelete.as_view(), name='event_delete'),
]
