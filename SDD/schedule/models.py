from django.db import models

class Showings(models.Model):
    showing_pkey = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=200)
    date = models.DateField('last time seen')
    time = models.TimeField('time shown')
    attendance = models.IntegerField()
    showing_id = models.IntegerField()
