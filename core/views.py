from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator as methodD
from .forms import ProfileForm
from .models import Movie, Profile


class Home(View):
   def get( self, request, *args, **kwargs ):
      if request.user.is_authenticated:
         return redirect('core:profile_list')
      return render( request, 'index.html' )

@methodD( login_required, name='dispatch' )
class Profiles(View):
   def get( self, request, *args, **kwargs ):
      profiles = request.user.profile.all()
      return render(request, 'profileList.html',
       { 'profiles': profiles })


@methodD( login_required, name='dispatch' )
class ProfileCreate(View):
   def get( self, request, *args, **kwargs ):
      # form for creating profile
      form = ProfileForm()

      return render( request, 'profileCreate.html', { 'form': form } )

   def post( self, request, *args, **kwargs ):
      form = ProfileForm(request.POST or None)
      if form.is_valid():
         profile = Profile.objects.create(**form.cleaned_data)
         if profile:
            request.user.profile.add(profile)
            return redirect('core:profile_list')

      return render( request, 'profileCreate.html', { 'form': form } )

# the profile's homepage
@methodD( login_required, name='dispatch' )
class Watch(View):
   def get( self, request, profile_id, *args, **kwargs ):
      try:
         profile = Profile.objects.get( uuid=profile_id )
         movies = Movie.objects.filter( age_limit=profile.age_limit )
         if profile not in request.user.profile.all():
            return redirect('core:profile_list')
         
         return render( request, 'movieList.html', { 'movies': movies } )
      except Profile.DoesNotExist:
            return redirect( 'core:profile_list' )


@methodD( login_required, name='dispatch' )
class ShowMovieDetail(View):
   def get( self, request, movie_id, *args, **kwargs ):
      try:
         movie = Movie.objects.get( uuid=movie_id )
         return render( request, 'movieDetail.html', { 'movie':movie })
      except Movie.DoesNotExist:
         return redirect('core:profile_list')


@methodD(login_required,name='dispatch')
class ShowMovie(View):
    def get(self,request,movie_id,*args, **kwargs):
        try:
            
            movie=Movie.objects.get(uuid=movie_id)

            movie=movie.videos.values()
          
            # remember to add a comment functionality

            return render(request,'showMovie.html',{
                'movie':list(movie)
            })
        except Movie.DoesNotExist:
            return redirect('core:profile_list')
