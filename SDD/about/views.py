from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def bylaws(request):
    template = loader.get_template('bylaws.html')
    context = { }
    return HttpResponse(template.render(context, request))

def faq(request):
    template = loader.get_template('faq.html')
    context = { }
    return HttpResponse(template.render(context, request))

def policies(request):
    template = loader.get_template('policies.html')
    context = { }
    return HttpResponse(template.render(context, request))
