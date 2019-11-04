from django.db import models

class Showings(models.Model):
    showing_pkey = models.AutoField(primary_key=True)
    date = models.DateField('last time seen')
    time = models.TimeField('time shown')
    attendance = models.IntegerField()
    showing_id = models.IntegerField()

    movie = models.ForeignKey(
        Movie,
        on_delete = models.CASCADE
    )

class Movie(models.Model):

    imdb_id = models.CharField(max_length=32, blank=False, null=False)
    title = models.CharField(max_length=2048, blank=False, null=False)
    year = models.CharField(max_length=16)
    mpaa_rating = models.CharField(max_length=8)
    runtime = models.CharField(max_length=16)
    genre = models.CharField(max_length=2048)
    actors = models.CharField(max_length=2048)
    writers = models.CharField(max_length=2048)
    directors = models.CharField(max_length=2048)
    plot = models.CharField(max_length=4096)
    poster_url = models.CharField(max_length=2048)
    trailer_url = models.CharField(max_length=2048)
    rotten_tomatoes_rating = models.CharField(max_length=32)
    image_path = models.CharField(max_length=2048)
