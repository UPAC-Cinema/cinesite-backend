from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import Showings
from .models import Movie
import datetime

def index(request):
    #showings_list = Showings.objects.filter(date__gte=datetime.date.today()).order_by('-date')
    showings_list = Showings.objects.order_by('-date')
    template = loader.get_template('index.html')

    json_serializer = serializers.get_serializer("json")()
    showings = json_serializer.serialize(showings_list)

    context = {
        'upcoming_showing1': showings_list[0],
        'upcoming_showing2': showings_list[1],
        'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))


def past_showings(request):
    showings_list = Showings.objects.order_by('-date')
    template = loader.get_template('schedule.html')
    context = {
        'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))

def generate_showing_string(movie):
    ...

def render_movie(request):
    template = loader.get_template('movie_info.html')

    movie_id = int(requests.GET["movie_id"])
    movie = ...

    movie_showings = ... # use a foreign key constraint in the showing model, then showings
                         #will be accessible from the movie object

    context = {
        'image_path':movie.image_path,
    'showings_string':generate_showing_string(movie),
    'trailer_url':movie.trailer,
    'description':movie.description
    }
