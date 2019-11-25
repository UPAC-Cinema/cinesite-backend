from django.test import TestCase
from django.test import Client
from django.contrib.messages import get_messages

class ContactTestCase(TestCase):
    def test_send_feedback_success_response(self):
        c = Client()
        response = c.post('/contact/feedback_results/', {'name': 'Corey D.', 'email': 'fakeemail@gmail.com', 'returned_text': 'This is a test email'})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 0)

    def test_send_feedback_fail_response(self):
        c = Client()
        response = c.post('/contact/feedback_results/', {'name': '', 'email': '', 'returned_text': ''})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You did not put in any feedback')

    def test_send_show_request_success_response(self):
        c = Client()
        response = c.post('/contact/sponsor_results/', {'orgName': 'test', 'contactName': 'test', 'contactEmail': 'test', 'desiredDate': 'test', 'year': 'test', 'firstChoice': 'test', 'secondChoice': 'test', 'thirdChoice': 'test', 'fourthChoice': 'test', 'unionYes': '', 'fiftyCheck': ''})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 0)

    def test_send_show_request_fail_response(self):
        c = Client()
        response = c.post('/contact/sponsor_results/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You did not fill in all required sections (marked by *)')
