from django.core.management import BaseCommand
from faker import Faker
from music.models import Artist, Album, Song, AlbumSong

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in range(10):
            artist = Artist.objects.create(name=fake.name())
            album = Album.objects.create(
                title=fake.sentence(nb_words=3),
                pub_year=fake.year(),
                artist=artist
            )
            for i in range(5):
                song = Song.objects.create(title=fake.word())
                AlbumSong.objects.create(album=album, song=song, track_number=i + 1)
