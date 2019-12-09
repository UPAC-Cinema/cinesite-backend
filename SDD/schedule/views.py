from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import Showings
from .models import Movie
import datetime

'''
    Index view for the schedule app is the main page that consumers will visit. This
    is the page that shows the next 2 movies in big format and displays a carousel
    of all the movies for the semester.
'''
def index(request):
    '''
        Grab the showings from the database in order to display them. Filter by
        anything on or after today, then reverse it so the front of the list is
        the next movie to be shown.
    '''
    showings_list = Showings.objects.order_by('-date').filter(date__gte=datetime.date.today()).reverse()

    if len(showings_list) == 0:
        ... # This is a bug!
    elif len(showings_list) == 1:
        ... # This is a bug!

    if len(showings_list) >= 1:
        upcoming_showing1 = showings_list[0]
    else:
        upcoming_showing1 = None

    if len(showings_list) >= 2:
        upcoming_showing2 = showings_list[1]
    else:
        upcoming_showing2 = None

    template = loader.get_template('index.html')


    json_serializer = serializers.get_serializer("json")()
    showings = json_serializer.serialize(showings_list)
    '''
        Context is a dictionary that is passed into the template for Django to
        use to load data inside of the HTML using python. We pass in the next
        two showings as a variable because it is easier to call in the template.
        We also pass the rest of the showings list to be used to generate the
        carousel.
    '''
    context = {
        'upcoming_showing1': upcoming_showing1,
        'upcoming_showing2': upcoming_showing2,
        'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))

'''
    past_showings view is for the page that displays the movies we have shown
    in the past along with their date and attendance (if we have it).
'''
def past_showings(request):
    '''
        Simply get showings_list by using filters to get it returned by date then
        movie title.
    '''
    showings_list = Showings.objects.order_by('-date').order_by('movie__title')
    template = loader.get_template('schedule.html')
    '''
        Context only passes in the sorted list here as we only need to print it
        out in the template in tabular format.
    '''
    context = {
        'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))
