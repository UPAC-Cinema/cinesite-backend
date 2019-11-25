'''
    A model is the single, definitive source of information about your data. It
    contains the essential fields and behaviors of the data you’re storing.
    Generally, each model maps to a single database table.

    For more information, please see:
        https://docs.djangoproject.com/en/2.2/topics/db/models/

    The basics:
    Each model is a Python class that subclasses django.db.models.Model.

    Each attribute of the model represents a database field. Example down below:
        imdb_id = models.CharField(max_length=32, blank=True, null=True)
        imdb_id is a COLUMN in the MOVIE TABLE. Its ATTRIBUTE is a CHARACTER 
        STRING of 32 MAX Length

    With all of this, Django gives you an automatically-generated database-access API

'''
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
