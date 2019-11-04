from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages

import smtplib
import datetime

def index(request):
    template = loader.get_template('sponsor.html')
    context = {
        # 'showings_list': showings_list,
    }
    return HttpResponse(template.render(context, request))

def results(request):
    if (request.POST.get('orgName') == ''):
        messages.info(request,
            'You did not fill in all required sections (marked by *)')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    elif (request.POST.get('contactName') == ''):
        messages.info(request,
            'You did not fill in all required sections (marked by *)')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    elif (request.POST.get('contactEmail') == ''):
        messages.info(request,
            'You did not fill in all required sections (marked by *)')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    elif (request.POST.get('unionYes') == None) and (request.POST.get('unionNo') == None):
        messages.info(request,
            'You did not fill in all required sections (marked by *)')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    elif (request.POST.get('fiftyCheck') == None) and (request.POST.get('fullCheck') == None):
        messages.info(request,
            'You did not fill in all required sections (marked by *)')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    elif (request.POST.get('desiredDate') == ''):
        messages.info(request,
            'You did not fill in all required sections (marked by *)')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    elif (request.POST.get('year') == ''):
        messages.info(request,
            'You did not fill in all required sections (marked by *)')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    elif (request.POST.get('firstChoice') == ''):
        messages.info(request,
            'You did not fill in all required sections (marked by *)')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        passed_dict = {
            'orgName': request.POST.get('orgName'),
            'contactName': request.POST.get('contactName'),
            'contactEmail': request.POST.get('contactEmail'),
            # 'unionYes': request.POST.get('unionYes'),
            # 'unionNo': request.POST.get('unionNo'),
            'desiredDate': request.POST.get('desiredDate'),
            'year': request.POST.get('year'),
            'firstChoice': request.POST.get('firstChoice'),
            'secondChoice': request.POST.get('secondChoice'),
            'thirdChoice': request.POST.get('thirdChoice'),
            'fourthChoice': request.POST.get('fourthChoice')

        }
        if (request.POST.get('unionYes') != None):
            passed_dict['union'] = 'union funded'
        if (request.POST.get('unionNo') != None):
            passed_dict['union'] = 'not union funded'
        if (request.POST.get('fiftyCheck') != None):
            passed_dict['payment'] = '50/50'
        if (request.POST.get('fullCheck') != None):
            passed_dict['payment'] = 'Full payment'



        sendemail_sponsor(passed_dict)
        return HttpResponseRedirect('/home')
        # return HttpResponse(request.POST.get('fourthChoice'))


def sendemail_sponsor(datadict):
    gmail_user = 'upac.cinemail@gmail.com'
    gmail_password = 'cinemaiscool'

    sent_from = gmail_user
    to = ['upac.cinemail@gmail.com']
    subject = datadict['orgName'] + "sponsorship request"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    Organziaton Name: %s
    Contact Name: %s
    Contact Email: %s
    Union Funded?: %s
    Payment Option: %s
    Desired Date: %s
    Year: %s
    First Choice: %s
    Second Choice: %s
    Third Choice: %s
    Fourth Choice: %s

    """ % (sent_from, to, subject, datadict['orgName'], datadict['contactName'],
    datadict['contactEmail'], datadict['union'], datadict['payment'],
    datadict['desiredDate'], datadict['year'], datadict['firstChoice'],
    datadict['secondChoice'], datadict['thirdChoice'], datadict['fourthChoice'])

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
            print ('Something went wrong...')
