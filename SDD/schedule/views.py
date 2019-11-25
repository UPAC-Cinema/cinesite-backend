from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import Showings
from .models import Movie
import datetime

def index(request):
    #showings_list = Showings.objects.filter(date__gte=datetime.date.today()).order_by('-date')
    showings_list = Showings.objects.order_by('-date').filter(date__gte=datetime.date.today()).reverse()

    if len(showings_list) == 0:
        ... # This is a bug!
    elif len(showings_list) == 1:
        ... # This is a bug!

    upcoming_showing1 = showings_list[0]
    upcoming_showing2 = showings_list[1]
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
    showings_list = Showings.objects.order_by('-date').order_by('movie__title')
    template = loader.get_template('schedule.html')
    context = {
        'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))
