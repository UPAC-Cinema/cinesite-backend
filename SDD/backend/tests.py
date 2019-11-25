from django.test import TestCase
from django.test import Client
from django.contrib.messages import get_messages
from schedule.models import Showings
from schedule.models import Movie

class BackendTestCase(TestCase):
    '''
        Test if adding a movie to the schedule with a correct input correctly
        updates the database
    '''
    def test_update_sched_success(self):
        c = Client()

        ''' Create a post request to end point '''
        response = c.post('/backend/update_sched/', {'title': 'The Night Comes for Us', 'year': '2018', 'showdate': '2005-06-07', 'showtimes': '7:00PM, 9:30PM, 12:00AM'})
        messages = list(get_messages(response.wsgi_request))

        ''' This should pass so there should be 0 messages '''
        self.assertEqual(len(messages), 0)

        ''' Find the movie & showing that we just added '''
        new_movie = Movie.objects.get(title='The Night Comes for Us')
        new_showing = Showings.objects.get(date='2005-06-07')

        ''' Since we found the movie and showing, all of these should pass '''
        self.assertEqual(new_movie.year, '2018')
        self.assertEqual(new_movie.directors, 'Timo Tjahjanto')
        self.assertEqual(new_movie.title, new_showing.movie.title)
        self.assertEqual(new_showing.time, '7:00PM, 9:30PM, 12:00AM')

    '''
        Test if adding a movie to the schedule with a incorrect input fails to
        save to database
    '''
    def test_update_sched_fail(self):
        c = Client()

        ''' Create a post request to end point '''
        response = c.post('/backend/update_sched/', {'title': '', 'year': '', 'showdate': '', 'showtimes': ''})
        messages = list(get_messages(response.wsgi_request))

        ''' This should not pass so there should be 1 message '''
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "You're missing some fields!")

    '''
        Test if editing attendance correctly works by creating a new movie then
        editing the attendance of that movie.
    '''
    def test_edit_attendance(self):
        c = Client()

        ''' Create a post request to end point '''
        c.post('/backend/update_sched/', {'title': 'The Night Comes for Us', 'year': '2018', 'showdate': '2005-06-07', 'showtimes': '7:00PM, 9:30PM, 12:00AM'})

        ''' Find the movie & showing we just uploaded '''
        new_movie = Movie.objects.get(title='The Night Comes for Us')
        new_showing = Showings.objects.get(date='2005-06-07')

        ''' showings when made have an attendance of -1 '''
        self.assertEqual(new_showing.attendance, -1)

        ''' Create a post request to end point '''
        response = c.post('/backend/edit/', {'id': new_showing.showing_pkey, 'attendance': 50})

        ''' Get the updated showing after editing the attendance '''
        new_showing = Showings.objects.get(date='2005-06-07')

        ''' Should be 50 now '''
        self.assertEqual(new_showing.attendance, 50)

    '''
        Test if deleting a showing actually deletes a showing from the database
        by making a new movie/showing then attempt to delete it.
    '''
    def test_delete_showing(self):
        c = Client()

        ''' Create a post request to end point '''
        c.post('/backend/update_sched/', {'title': 'The Night Comes for Us', 'year': '2018', 'showdate': '2005-06-07', 'showtimes': '7:00PM, 9:30PM, 12:00AM'})

        ''' Find the movie & showing we just uploaded '''
        new_movie = Movie.objects.get(title='The Night Comes for Us')
        new_showing = Showings.objects.get(date='2005-06-07')

        showing_num = Showings.objects.all().count()
        movies_num = Movie.objects.all().count()

        '''
            The amount of movies and showings in the database should be 1.
            This is because a fake database is created to do testing in.
        '''
        self.assertEqual(showing_num, 1)
        self.assertEqual(movies_num, 1)

        ''' Create a get request to end point '''
        c.get('/backend/delete/', {'id': new_showing.showing_pkey})

        ''' Get all showings and movies '''
        showing_num = Showings.objects.all().count()
        movies_num = Movie.objects.all().count()

        '''
        Showings should be 0 now since we deleted the showing
        Movies should still be 1 since we dont delete movies from the database
        '''
        self.assertEqual(showing_num, 0)
        self.assertEqual(movies_num, 1)
