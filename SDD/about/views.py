from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def bylaws(request):
    template = loader.get_template('bylaws.html')
    context = {
        # 'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))

def faq(request):
    template = loader.get_template('faq.html')
    context = {
        # 'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))

def policy(request):
    template = loader.get_template('policies.html')
    context = {
        # 'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))
