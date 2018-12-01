from django.shortcuts import render
from musicApp.models import Artist, Album, Song


def artist_view(request):
    id = request.GET['id']
    data = Artist.objects.filter(genre=id)
    return render(request, 'musicApp_extension/artist_page.html', {'data': data})


def user_artist_view(request):
    artist_added_by = request.user.username
    data = Artist.objects.filter(artist_added_by=artist_added_by)
    return render(request, 'musicApp_extension/user_artist_page.html', {'data': data})


def album_view(request):
    id = request.GET['id']
    data = Album.objects.filter(artist=id)
    return render(request, 'musicApp_extension/album_page.html', {'data': data})


def user_album_view(request):
    album_added_by = request.user.username
    data = Album.objects.filter(album_added_by=album_added_by)
    return render(request, 'musicApp_extension/user_album_page.html', {'data': data})


def song_view(request):
    id = request.GET['id']
    data = Song.objects.filter(album=id)
    return render(request, 'musicApp_extension/song_page.html', {'data': data})


def user_song_view(request):
    song_added_by = request.user.username
    data = Song.objects.filter(song_added_by=song_added_by)
    return render(request, 'musicApp_extension/user_song_page.html', {'data': data})

