from django.shortcuts import render, redirect
from .forms import GenreForm, ArtistForm, AlbumForm, SongForm
from musicApp.views import genre_view
from musicApp_extension.views import user_artist_view, user_album_view, user_song_view
from django.contrib.auth.decorators import login_required
from musicApp.models import Genre, Artist, Album, Song


@login_required(login_url='login')
def genre_create(request):
    form = GenreForm()
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre_obj = Genre()
            genre_obj.artist_genre = form.cleaned_data['artist_genre']
            genre_obj.genre_added_by = request.user.username
            genre_obj.save()
            return redirect(genre_view)
    return render(request, 'crud/create_genre_page.html', {'form': form})


@login_required(login_url='login')
def artist_create(request):
    form = ArtistForm()
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist_obj = Artist()
            artist_obj.genre = form.cleaned_data['genre']
            artist_obj.artist_name = form.cleaned_data['artist_name']
            artist_obj.artist_added_by = request.user.username
            artist_obj.save()
            return redirect(user_artist_view)
    return render(request, 'crud/create_artist_page.html', {'form': form})


@login_required(login_url='login')
def album_create(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album_obj = Album()
            album_obj.artist = form.cleaned_data['artist']
            album_obj.album_title = form.cleaned_data['album_title']
            album_obj.album_logo = form.cleaned_data['album_logo']
            album_obj.album_released = form.cleaned_data['album_released']
            album_obj.album_added_by = request.user.username
            album_obj.save()
            return redirect(user_album_view)
    return render(request, 'crud/create_album_page.html', {'form': form})


@login_required(login_url='login')
def song_create(request):
    form = SongForm()
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song_obj = Song()
            song_obj.album = form.cleaned_data['album']
            song_obj.song_title = form.cleaned_data['song_title']
            song_obj.file_type = 'mp4'
            song_obj.song_url = form.cleaned_data['song_url'].split('=')[-1]
            song_obj.song_added_by = request.user.username
            song_obj.save()
            return redirect(user_song_view)
    return render(request, 'crud/create_song_page.html', {'form': form})

