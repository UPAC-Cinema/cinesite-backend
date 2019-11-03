from django.urls import path

from . import views

app_name = 'sponsor'
urlpatterns = [
    path('', views.index, name='index'),
]
