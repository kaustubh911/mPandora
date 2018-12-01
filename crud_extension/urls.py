from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^delete_genre$', views.genre_delete, name='delete_genre'),
    url(r'^delete_artist$', views.artist_delete, name='delete_artist'),
    url(r'^delete_album$', views.album_delete, name='delete_album'),
    url(r'^delete_song$', views.song_delete, name='delete_song'),
]