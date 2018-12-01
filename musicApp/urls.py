from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^genre$', views.genre_view, name='genre'),
    url(r'^signup$', views.sign_up, name='signup'),
    url(r'^login$', views.user_log_in, name='login'),
    url(r'^logout$', views.user_log_out, name='logout'),
    url(r'^user_genre$', views.user_genre_view, name='user_genre'),
    url(r'^update_genre$', views.genre_update, name='update_genre'),
    url(r'^update_artist$', views.artist_update, name='update_artist'),
    url(r'^update_album$', views.album_update, name='update_album'),
    url(r'^update_song$', views.song_update, name='update_song'),
]