from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from schedule.models import Showings
from schedule.models import Movie
import omdb
import json

def officers(request):
    template = loader.get_template('officers.html')
    context = {
        # 'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))

def update_sched(request):
    if (request.POST.get('title') == '' or request.POST.get('year') == '' or request.POST.get('showdate') == '' or request.POST.get('showtimes') == ''):
        messages.info(request, "You're missing some fields!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        movie_title = request.POST.get('title')
        movie_year = request.POST.get('year')
        movie = Movie.objects.all().filter(title=movie_title).filter(year=movie_year).first()

        if movie == None:
            r = omdb.request(t=movie_title, y=movie_year, plot='short', r='json', apikey='7e685318')
            result = json.loads(r.content)
            if result['Response'] == 'False':
                messages.info(request, "Movie not found in database...")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            score = '-1'
            for rating in result['Ratings']:
                if rating['Source'] == 'Rotten Tomatoes':
                    score = rating['Value']
            movie = Movie(imdb_id=result['imdbID'], title=movie_title, year=movie_year, mpaa_rating=result['Rated'], runtime=result['Runtime'], genre=result['Genre'], actors=result['Actors'], writers=result['Writer'], directors=result['Director'], plot=result['Plot'], poster_url=result['Poster'], trailer_url='None', rotten_tomatoes_rating=score, image_path='None')
            movie.save()

        showtimes = request.POST.get('showtimes').split(',')
        id = Showings.objects.all().count()
        showtime = Showings(date=request.POST.get('showdate'), time=request.POST.get('showtimes'), attendance=-1, showing_id=id, movie=movie)
        showtime.save()

        return HttpResponseRedirect('/backend')
