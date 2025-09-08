from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, related_name="album", on_delete=models.CASCADE)
    pub_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, related_name="album_songs", on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name="song_almubs", on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField()

    class Meta:
        unique_together = ("album", "track_number")
        ordering = ["track_number"]

    def __str__(self):
        return f"{self.album} - {self.song}"
