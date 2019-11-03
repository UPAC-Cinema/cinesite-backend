from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('bylaws.html')
    context = {
        # 'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))
