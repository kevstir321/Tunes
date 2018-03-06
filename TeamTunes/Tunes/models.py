from django.db import models
import uuid 

# Create your models here.
class User(models.Model):
	"""
	Model representing a user of the site. 
	"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this user")
	name = models.CharField(max_length=100)
	bio = models.TextField()
	events_hosting = models.ForeignKey('Event', blank = True, null = True, on_delete=models.SET_NULL, related_name = "user_events_hosting")
	events_attending = models.ManyToManyField('Event', related_name = "user_events_attending") 
	events_attended = models.ManyToManyField('Event', related_name = "user_events_attended")
	anthem = models.ForeignKey('Song', on_delete=models.SET_NULL, null = True, related_name = "user_anthem")
	location = models.CharField(max_length=100)
	followers = models.ManyToManyField('User', related_name = "user_followers")
	following = models.ManyToManyField('User', related_name = "user_following")
	favorite_albums = models.CharField(max_length=200)
	favorite_songs = models.ManyToManyField('Song')
	favorite_genres = models.CharField(max_length=200)
	hobbies = models.CharField(max_length=200)
	email = models.EmailField()
	current_song = models.ForeignKey('Song', blank = True, null = True, on_delete=models.SET_NULL, related_name = "user_current_song")

	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.name

	def get_absolute_url(self):
		"""
		Returns the url to access a particular user instance.
		"""
		return reverse('user-detail', args=[str(self.id)])
	
class Event(models.Model):
	"""
	Model representing an event listing.
	"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this event")
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField()#upload_to=)
	host = models.ForeignKey('User', on_delete=models.CASCADE, related_name = "event_host")
	people = models.ManyToManyField('User', related_name = "people_attending")
	
	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.name

	def get_absolute_url(self):
		"""
		Returns the url to access a particular event instance.
		"""
		return reverse('event-detail', args=[str(self.id)])

class Song(models.Model):
	"""
	Model representing a song.
	"""
	name = models.CharField(max_length=100)
	artist = models.CharField(max_length=100)
	album = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	art = models.ImageField()#upload_to=)
	
	def __str__(self):
		"""
		String for representing the Model object (in Admin site etc.)
		"""
		return self.name

	def get_absolute_url(self):
		"""
		Returns the url to access a particular song instance.
		"""
		return reverse('song-detail', args=[str(self.id)])