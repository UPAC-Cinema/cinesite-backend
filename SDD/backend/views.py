from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def officers(request):
    template = loader.get_template('officers.html')
    context = {
        # 'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))