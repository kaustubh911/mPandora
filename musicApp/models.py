from django.db import models


class Genre(models.Model):
    artist_genre = models.CharField(max_length=200, unique=True)
    genre_added_by = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + '. ' + self.artist_genre


class Artist(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=200, unique=True)
    artist_added_by = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + '. ' + self.artist_name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=200, unique=True)
    album_logo = models.CharField(max_length=500)
    album_released = models.CharField(max_length=10)
    album_added_by = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + '. ' + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200, unique=True)
    file_type = models.CharField(max_length=20)
    song_url = models.CharField(max_length=500)
    song_added_by = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + '. ' + self.song_title
