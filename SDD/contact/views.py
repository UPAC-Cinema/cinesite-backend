from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages

import smtplib
import datetime

'''
    Feedback view is for the page that provides users with a form to send the
    club feedback on their experience with a movie night or with officers of the
    club.
'''
def feedback(request):
    '''
        No context needed so simply just render the page for the user.
    '''
    template = loader.get_template('feedback.html')
    context = {}
    return HttpResponse(template.render(context, request))

'''
    feedback_results view is a page that the user never sees. It is the inbetween
    when a user presses submit. Upon successful form completion, user is sent to
    home page. Upon failure of form completion, user is sent back to feedback page.
'''
def feedback_results(request):
    '''
        Check if the user has inputed data into the required text category.
        If they have:
            Make a dictionary containing name, email, and the input text.
            pass this dictionary to helper function sendemail_feedback.
            Then redirect to homepage.
        If they have not:
            Post an error message
            Redirect to feedback page.
    '''
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
        return HttpResponseRedirect('/')

def sponsor(request):
    '''
        No context needed so simply just render the page for the user.
    '''
    template = loader.get_template('sponsor.html')
    context = {}
    return HttpResponse(template.render(context, request))

'''
    sponser_results view is a page that the user never sees. It is the inbetween
    when a user presses submit. Upon successful form completion, user is sent to
    home page. Upon failure of form completion, user is sent back to sponsor page.
'''
def sponsor_results(request):
    '''
        Error Checking for form completion. If any of the required fields fail,
        Output error message and redirect to sponsor page.
    '''
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
        '''
            If all fields filled out correctly, then make a dictionary of data then
            pass it to sendemail_sponsor to send an email to the club.
        '''
    else:
        passed_dict = {
            'orgName': request.POST.get('orgName'),
            'contactName': request.POST.get('contactName'),
            'contactEmail': request.POST.get('contactEmail'),
            'desiredDate': request.POST.get('desiredDate'),
            'year': request.POST.get('year'),
            'firstChoice': request.POST.get('firstChoice'),
            'secondChoice': request.POST.get('secondChoice'),
            'thirdChoice': request.POST.get('thirdChoice'),
            'fourthChoice': request.POST.get('fourthChoice')

        }
        '''
            Special checking for form elements that involve input buttons rather
            than input text
        '''
        if (request.POST.get('unionYes') != None):
            passed_dict['union'] = 'union funded'
        if (request.POST.get('unionNo') != None):
            passed_dict['union'] = 'not union funded'
        if (request.POST.get('fiftyCheck') != None):
            passed_dict['payment'] = '50/50'
        if (request.POST.get('fullCheck') != None):
            passed_dict['payment'] = 'Full payment'

        sendemail_sponsor(passed_dict)
        return HttpResponseRedirect('/')


'''
    Helper function to send emails using data from sponsor forms
'''
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
    '''
        Try to send the email by logging in first, If anything fails, error is
        sent to server.
    '''
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
            print ('Something went wrong...')

'''
    Helper function to send emails using data from feedback forms
'''
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
    '''
        Try to send the email by logging in first, If anything fails, error is
        sent to server.
    '''
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
            print ('Something went wrong...')
