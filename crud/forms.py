from django import forms
from musicApp.models import Genre, Artist, Album, Song


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('artist_genre',)


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('genre', 'artist_name')


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'album_title', 'album_logo', 'album_released')


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('album', 'song_title', 'song_url')
