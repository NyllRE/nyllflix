from django.urls import path
from .views import *

app_name='core'

urlpatterns = [
	path( '', Home.as_view() ),
	path( 'profile/', Profiles.as_view(), name='profile_list' ),
	path( 'profile/create/', ProfileCreate.as_view(), name='profile_create' ),
	path( 'watch/detail/<str:movie_id>/', ShowMovieDetail.as_view(), name='movie_detail' ),
	path( 'movie/<str:profile_id>/', Watch.as_view(), name='watch' ),
	path( 'movie/play/<str:movie_id>/', ShowMovie.as_view(), name='play' ),
]
