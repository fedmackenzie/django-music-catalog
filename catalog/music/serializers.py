from rest_framework import serializers
from .models import Artist, Album, Song, AlbumSong


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title"]


class AlbumSongSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)
    song_id = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), source="song", write_only=True)

    class Meta:
        model = AlbumSong
        fields = ["id", "track_number", "song", "song_id"]


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(), source="artist", write_only=True)
    songs = AlbumSongSerializer(source="album_songs", many=True, read_only=True)

    class Meta:
        model = Album
        fields = ["id", "title", "pub_year", "artist", "artist_id", "songs"]


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ["id", "name", "albums"]
