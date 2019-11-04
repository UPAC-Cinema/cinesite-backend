from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def feedback(request):
    template = loader.get_template('feedback.html')
    context = { }
    return HttpResponse(template.render(context, request))

def sponsor(request):
    template = loader.get_template('sponsor.html')
    context = { }
    return HttpResponse(template.render(context, request))
