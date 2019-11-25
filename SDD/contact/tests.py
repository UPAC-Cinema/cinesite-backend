from django.test import TestCase
from django.test import Client
from django.contrib.messages import get_messages

class ContactTestCase(TestCase):
    '''
        Test if inputing correct data to feedback form works via simulating a
        post to end point
    '''
    def test_send_feedback_success_response(self):
        c = Client()

        ''' Create a post request to end point '''
        response = c.post('/contact/feedback_results/', {'name': 'Corey D.', 'email': 'fakeemail@gmail.com', 'returned_text': 'This is a test email'})
        messages = list(get_messages(response.wsgi_request))
        
        ''' This should pass so there should be 0 messages '''
        self.assertEqual(len(messages), 0)

    '''
        Test if inputing incorrect data to feedback form does not work via
        simulating a post to end point
    '''
    def test_send_feedback_fail_response(self):
        c = Client()

        ''' Create a post request to end point '''
        response = c.post('/contact/feedback_results/', {'name': '', 'email': '', 'returned_text': ''})
        messages = list(get_messages(response.wsgi_request))

        ''' This should not pass so there should be 1 message '''
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You did not put in any feedback')

    '''
        Test if inputing correct data to sponsor form works via simulating a
        post to end point
    '''
    def test_send_show_request_success_response(self):
        c = Client()
        ''' Create a post request to end point '''
        response = c.post('/contact/sponsor_results/', {'orgName': 'test', 'contactName': 'test', 'contactEmail': 'test', 'desiredDate': 'test', 'year': 'test', 'firstChoice': 'test', 'secondChoice': 'test', 'thirdChoice': 'test', 'fourthChoice': 'test', 'unionYes': '', 'fiftyCheck': ''})
        messages = list(get_messages(response.wsgi_request))

        ''' This should pass so there should be 0 messages '''
        self.assertEqual(len(messages), 0)

    '''
        Test if inputing incorrect data to sponsor form does not work via
        simulating a post to end point
    '''
    def test_send_show_request_fail_response(self):
        c = Client()

        ''' Create a post request to end point '''
        response = c.post('/contact/sponsor_results/')
        messages = list(get_messages(response.wsgi_request))

        ''' This should not pass so there should be 1 message '''
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You did not fill in all required sections (marked by *)')
