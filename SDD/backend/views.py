from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from schedule.models import Showings
from schedule.models import Movie
import omdb
import json
import sys
import os
from os.path import expanduser, join
from os import makedirs
'''
    Helper Function to determine what OS the user is using. It then returns a
    path to where data should be stored on the user's system
'''
def appdata():
    path = "cinesite"

    if sys.platform.startswith("linux"):
        path = join(expanduser("~"), ".local/share/cinesite")
    elif sys.platform == "win32":
        path = join(os.getenv('APPDATA'), "cinesite")

    makedirs(path, exist_ok=True)
    return path
'''
    Writes file to appdata of user using path determined from appdata function
'''
def write_to_disk(f, name):
    with open(join(appdata(), name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

'''
    Allows the user to upload a PDF to the server to change the displayed Bylaws PDF.
'''
def bylaws(request):
    if request.method == 'POST':
        write_to_disk(request.FILES['bylaws'], "bylaws.pdf")
        return HttpResponseRedirect('/backend')
    else:
        bylaws_file = open(join(appdata(), 'bylaws.pdf'), 'rb')
        response = HttpResponse(content=bylaws_file)
        response['Content-Type'] = 'application/pdf'
        return response

'''
    Allows the user to upload a PDF to the server to change the displayed Policy PDF.
'''
def policies(request):
    if request.method == 'POST':
        write_to_disk(request.FILES['policies'], "policies.pdf")
        return HttpResponseRedirect('/backend')
    else:
        policies_file = open(join(appdata(), 'policies.pdf'), 'rb')
        response = HttpResponse(content=policies_file)
        response['Content-Type'] = 'application/pdf'
        return response

'''
    Allows the user to upload a PDF to the server to change the displayed FAQ PDF.
'''
def faqs(request):
    if request.method == 'POST':
        write_to_disk(request.FILES['faqs'], "faqs.pdf")
        return HttpResponseRedirect('/backend')
    else:
        faqs_file = open(join(appdata(), 'faqs.pdf'), 'rb')
        response = HttpResponse(content=faqs_file)
        response['Content-Type'] = 'application/pdf'
        return response
'''
    Pressing the delete button on past_showings page will call this functionm
    then remove the entry from the database.
'''
def delete(request):
    Showings.objects.filter(showing_pkey=request.GET['id']).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


'''
    Pressing the edit button on past_showings page will call this functionm
    then allow user to put the attendance in to the entry.
'''
def edit(request):
    if request.method == 'POST':
        showing_pkey = request.POST['id']
        attendance = request.POST['attendance']

        showing = Showings.objects.get(showing_pkey=showing_pkey)
        showing.attendance = attendance
        showing.save()

        return HttpResponseRedirect('/past_showings/')
    else:
        showing_pkey = request.GET['id']
        showing = Showings.objects.get(showing_pkey=showing_pkey)
        template = loader.get_template('edit_showing.html')
        context = {
            'showing': showing,
            'id': showing_pkey
        }
        return HttpResponse(template.render(context, request))

'''
    This is the view used for the officers page.
'''
def officers(request):
    template = loader.get_template('officers.html')
    context = {}
    return HttpResponse(template.render(context, request))

'''
    This function provides officers with the ability to add a movie into the
    database schedule. The user will need to type in the correct movie name
    along with the correct year. After that, they will select the date it will
    be shown by UPAC cinema. Then they will select the type of showing based on
    movie length.
'''
def update_sched(request):
    ''' Error checking for if user doesnt put all fields in '''
    if (request.POST.get('title') == '' or request.POST.get('year') == '' or request.POST.get('showdate') == '' or request.POST.get('showtimes') == ''):
        messages.info(request, "You're missing some fields!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        movie_title = request.POST.get('title')
        movie_year = request.POST.get('year')
        ''' Check to see if movie exists in database already '''
        movie = Movie.objects.all().filter(title=movie_title).filter(year=movie_year).first()

        ''' If movie does not exist in database... '''
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
        
        ''' make a showing database entry then save it '''
        showtime = Showings(date=request.POST.get('showdate'), time=request.POST.get('showtimes'), attendance=-1, showing_id=id, movie=movie)
        showtime.save()

        return HttpResponseRedirect('/backend')
