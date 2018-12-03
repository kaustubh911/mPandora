from django import forms
from .models import Genre, Artist, Album, Song


class SignUp(forms.Form):
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateGenre(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('artist_genre',)


class UpdateArtist(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('genre', 'artist_name')


class UpdateAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'album_title', 'album_logo', 'album_released')


class UpdateSong(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('album', 'song_title', 'song_url')
