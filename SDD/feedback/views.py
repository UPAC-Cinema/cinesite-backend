from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages

import smtplib
import datetime

def index(request):
    template = loader.get_template('feedback.html')
    context = {
        # 'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))

def results(request):
    if (request.POST.get('returned_text') == ''):
        messages.info(request, 'You did not put in any feedback')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        passed_dict = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'returned_text': request.POST.get('returned_text')
        }
        sendemail_feedback(passed_dict)
        return HttpResponseRedirect('/home')

def sendemail_feedback(datadict):
    gmail_user = 'upac.cinemail@gmail.com'
    gmail_password = 'cinemaiscool'

    sent_from = gmail_user
    to = ['upac.cinemail@gmail.com']
    subject = 'Feedback recieved on' + str(datetime.datetime.today())
    body = datadict['returned_text']
    name = datadict['name']
    email = datadict['email']

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    Name: %s
    Email: %s

    Feedback: %s

    """ % (sent_from, to, subject, name, email, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
            print ('Something went wrong...')
