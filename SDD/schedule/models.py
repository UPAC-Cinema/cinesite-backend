from django.db import models

class Movie(models.Model):
    imdb_id = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=2048, blank=True, null=True)
    year = models.CharField(max_length=16, blank=True, null=True)
    mpaa_rating = models.CharField(max_length=16, blank=True, null=True)
    runtime = models.CharField(max_length=16, blank=True, null=True)
    genre = models.CharField(max_length=2048, blank=True, null=True)
    actors = models.CharField(max_length=2048, blank=True, null=True)
    writers = models.CharField(max_length=2048, blank=True, null=True)
    directors = models.CharField(max_length=2048, blank=True, null=True)
    plot = models.CharField(max_length=4096, blank=True, null=True)
    poster_url = models.CharField(max_length=2048, blank=True, null=True)
    trailer_url = models.CharField(max_length=2048, blank=True, null=True)
    rotten_tomatoes_rating = models.CharField(max_length=32, blank=True, null=True)
    image_path = models.CharField(max_length=2048, blank=True, null=True)

class Showings(models.Model):
    showing_pkey = models.AutoField(primary_key=True)
    date = models.DateField('last time seen')
    time = models.CharField(max_length=204, blank=True, null=True)
    attendance = models.IntegerField()
    showing_id = models.IntegerField()

    movie = models.ForeignKey(
        Movie,
        on_delete = models.CASCADE
    )
