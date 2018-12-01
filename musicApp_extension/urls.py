from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^artist$', views.artist_view, name='artist'),
    url(r'^user_artist$', views.user_artist_view, name='user_artist'),
    url(r'^album$', views.album_view, name='album'),
    url(r'^user_album$', views.user_album_view, name='user_album'),
    url(r'^song$', views.song_view, name='song'),
    url(r'^user_song$', views.user_song_view, name='user_song'),
]