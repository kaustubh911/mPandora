from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_genre$', views.genre_create, name='create_genre'),
    url(r'^create_artist$', views.artist_create, name='create_artist'),
    url(r'^create_album$', views.album_create, name='create_album'),
    url(r'^create_song$', views.song_create, name='create_song'),
]