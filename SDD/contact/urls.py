from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [
    path('/feedback', views.feedback, name='feedback'),
    path('/sponsor', views.sponsor, name='sponsor'),
]
