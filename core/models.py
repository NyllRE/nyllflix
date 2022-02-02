from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
   profile = models.ManyToManyField( 'Profile', blank=True )

   # def __str__(self):
   #       return self.profile.name


AGE_CHOICES = (
   ('All', 'All'),
   ('Kids', 'Kids')
)
class Profile(models.Model):
   uuid      = models.UUIDField( default=uuid.uuid4 )
   name      = models.CharField( max_length=225 )
   age_limit = models.CharField( max_length=10, choices=AGE_CHOICES )

   def __str__(self):
         return self.name

MOVIE_CHOICES = (
   ('seasonal', 'Seasonal'),
   ('single', 'Single')
)
class Movie(models.Model):
   uuid        = models.UUIDField( default=uuid.uuid4 )
   title       = models.CharField( max_length=225 )
   description = models.TextField( blank=True, null=True )
   type        = models.CharField( max_length=10, choices=MOVIE_CHOICES )
   created     = models.DateTimeField( auto_now_add=True )
   videos      = models.ManyToManyField( 'Video' )
   flyer       = models.ImageField( upload_to='flyers' )
   age_limit   = models.CharField( max_length=10, choices=AGE_CHOICES )

   def __str__(self):
         return self.title


class Video(models.Model):
   title = models.CharField( max_length=255, blank=True, null=True )
   file  = models.FileField( upload_to='movies' )

   def __str__(self):
         return self.title
   