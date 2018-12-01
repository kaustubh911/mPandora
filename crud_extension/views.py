from django.shortcuts import redirect
from musicApp.models import Genre, Artist, Album, Song
from django.contrib.auth.decorators import login_required
from musicApp.views import user_genre_view, user_artist_view, user_album_view, user_song_view


@login_required(login_url='login')
def genre_delete(request):
    id = request.GET['id']
    data = Genre.objects.get(id=id)
    data.delete()
    return redirect(user_genre_view)


@login_required(login_url='login')
def artist_delete(request):
    id = request.GET['id']
    data = Artist.objects.get(id=id)
    data.delete()
    return redirect(user_artist_view)


@login_required(login_url='login')
def album_delete(request):
    id = request.GET['id']
    data = Album.objects.get(id=id)
    data.delete()
    return redirect(user_album_view)


@login_required(login_url='login')
def song_delete(request):
    id = request.GET['id']
    data = Song.objects.get(id=id)
    data.delete()
    return redirect(user_song_view)
