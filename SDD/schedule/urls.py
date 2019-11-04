from django.urls import path

from . import views

app_name = 'schedule'
urlpatterns = [
    path('', views.index, name='index'),
    path('past_showings/', views.past_showings, name='past_showings'),
]
