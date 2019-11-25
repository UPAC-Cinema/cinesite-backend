from django.test import TestCase
from django.test import Client
from django.contrib.messages import get_messages
from schedule.models import Showings
from schedule.models import Movie

class BackendTestCase(TestCase):
    def test_update_sched_success(self):
        c = Client()
        response = c.post('/backend/update_sched/', {'title': 'The Night Comes for Us', 'year': '2018', 'showdate': '2005-06-07', 'showtimes': '7:00PM, 9:30PM, 12:00AM'})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 0)

        new_movie = Movie.objects.get(title='The Night Comes for Us')
        new_showing = Showings.objects.get(date='2005-06-07')

        self.assertEqual(new_movie.year, '2018')
        self.assertEqual(new_movie.directors, 'Timo Tjahjanto')
        self.assertEqual(new_movie.title, new_showing.movie.title)
        self.assertEqual(new_showing.time, '7:00PM, 9:30PM, 12:00AM')

    def test_update_sched_fail(self):
        c = Client()
        response = c.post('/backend/update_sched/', {'title': '', 'year': '', 'showdate': '', 'showtimes': ''})
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "You're missing some fields!")

    def test_edit_attendance(self):
        c = Client()
        c.post('/backend/update_sched/', {'title': 'The Night Comes for Us', 'year': '2018', 'showdate': '2005-06-07', 'showtimes': '7:00PM, 9:30PM, 12:00AM'})
        new_movie = Movie.objects.get(title='The Night Comes for Us')
        new_showing = Showings.objects.get(date='2005-06-07')
        self.assertEqual(new_showing.attendance, -1)

        response = c.post('/backend/edit/', {'id': new_showing.showing_pkey, 'attendance': 50})
        new_showing = Showings.objects.get(date='2005-06-07')
        self.assertEqual(new_showing.attendance, 50)

    def test_delete_showing(self):
        c = Client()
        c.post('/backend/update_sched/', {'title': 'The Night Comes for Us', 'year': '2018', 'showdate': '2005-06-07', 'showtimes': '7:00PM, 9:30PM, 12:00AM'})
        new_movie = Movie.objects.get(title='The Night Comes for Us')
        new_showing = Showings.objects.get(date='2005-06-07')

        showing_num = Showings.objects.all().count()
        movies_num = Movie.objects.all().count()
        self.assertEqual(showing_num, 1)
        self.assertEqual(movies_num, 1)

        c.get('/backend/delete/', {'id': new_showing.showing_pkey})
        showing_num = Showings.objects.all().count()
        movies_num = Movie.objects.all().count()
        self.assertEqual(showing_num, 0)
        self.assertEqual(movies_num, 1)
