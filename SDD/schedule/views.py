from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Showings

def index(request):
    showings_list = Showings.objects.order_by('-date').reverse()
    template = loader.get_template('schedule.html')
    context = {
        'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))
