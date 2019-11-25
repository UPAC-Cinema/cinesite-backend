from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

'''
    bylaws view displays the bylaws page for the user.
'''
def bylaws(request):
    '''
        No context needed so simply just render the page for the user.
    '''
    template = loader.get_template('bylaws.html')
    context = {}
    return HttpResponse(template.render(context, request))

'''
    faq view displays the faq page for the user.
'''
def faq(request):
    '''
        No context needed so simply just render the page for the user.
    '''
    template = loader.get_template('faq.html')
    context = {}
    return HttpResponse(template.render(context, request))

'''
    policy view displays the policies page for the user.
'''
def policy(request):
    '''
        No context needed so simply just render the page for the user.
    '''
    template = loader.get_template('policies.html')
    context = {}
    return HttpResponse(template.render(context, request))
