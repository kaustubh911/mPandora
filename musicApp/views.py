from django.shortcuts import render, redirect
from .models import Genre, Artist, Album, Song
from django.contrib.auth.models import User
from .forms import UserLoginForm, UpdateGenre, UpdateArtist, UpdateAlbum, UpdateSong, SignUp
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from musicApp_extension.views import user_artist_view, user_album_view, user_song_view


def home(request):
    return render(request, 'musicApp/home.html')


def genre_view(request):
    data = Genre.objects.all()
    return render(request, 'musicApp/genre_page.html', {'data': data})


def sign_up(request):
    form = SignUp()
    message = ''
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username__iexact=username).exists():
                return render(request, 'musicApp/sign_up_error.html')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User()
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.set_password(password)
            user.save()
            message = 'User : ' + username + ' registered successfully !'
    return render(request, 'musicApp/signup_page.html', {'form': form, 'msg': message})


def user_log_in(request):
    if request.user.username:
        return redirect(home)
    form = UserLoginForm()
    message = ''
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                message = 'Invalid log in details !'
            else:
                login(request, user)
                return redirect(genre_view)
    return render(request, 'musicApp/login_page.html', {'form': form, 'msg': message})


def user_log_out(request):
    logout(request)
    return redirect(user_log_in)


def user_genre_view(request):
    genre_added_by = request.user.username
    data = Genre.objects.filter(genre_added_by=genre_added_by)
    return render(request, 'musicApp/user_genre_page.html', {'data': data})


@login_required(login_url='login')
def genre_update(request):
    id = request.GET['id']
    data = Genre.objects.get(id=id)
    form = UpdateGenre(instance=data)
    if request.method == 'POST':
        form = UpdateGenre(request.POST, instance=data)
        if form.is_valid():
            genre_obj = Genre()
            genre_obj.id = id
            genre_obj.artist_genre = form.cleaned_data['artist_genre']
            genre_obj.genre_added_by = request.user.username
            genre_obj.save()
            return redirect(user_genre_view)
    return render(request, 'musicApp/update_genre_page.html', {'form': form})


@login_required(login_url='login')
def artist_update(request):
    id = request.GET['id']
    data = Artist.objects.get(id=id)
    form = UpdateArtist(instance=data)
    if request.method == 'POST':
        form = UpdateArtist(request.POST, instance=data)
        if form.is_valid():
            artist_obj = Artist()
            artist_obj.id = id
            artist_obj.genre = form.cleaned_data['genre']
            artist_obj.artist_name = form.cleaned_data['artist_name']
            artist_obj.artist_added_by = request.user.username
            artist_obj.save()
            return redirect(user_artist_view)
    return render(request, 'musicApp/update_artist_page.html', {'form': form})


@login_required(login_url='login')
def album_update(request):
    id = request.GET['id']
    data = Album.objects.get(id=id)
    form = UpdateAlbum(instance=data)
    if request.method == 'POST':
        form = UpdateAlbum(request.POST, instance=data)
        if form.is_valid():
            album_obj = Album()
            album_obj.id = id
            album_obj.artist = form.cleaned_data['artist']
            album_obj.album_title = form.cleaned_data['album_title']
            album_obj.album_logo = form.cleaned_data['album_logo']
            album_obj.album_released = form.cleaned_data['album_released']
            album_obj.album_added_by = request.user.username
            album_obj.save()
            return redirect(user_album_view)
    return render(request, 'musicApp/update_album_page.html', {'form': form})


@login_required(login_url='login')
def song_update(request):
    id = request.GET['id']
    data = Song.objects.get(id=id)
    form = UpdateSong(instance=data)
    if request.method == 'POST':
        form = UpdateSong(request.POST, instance=data)
        if form.is_valid():
            song_obj = Song()
            song_obj.id = id
            song_obj.album = form.cleaned_data['album']
            song_obj.song_title = form.cleaned_data['song_title']
            song_obj.file_type = 'mp4'
            song_obj.song_url = form.cleaned_data['song_url'].split('=')[-1]
            song_obj.song_added_by = request.user.username
            song_obj.save()
            return redirect(user_song_view)
    return render(request, 'musicApp/update_song_page.html', {'form': form})
