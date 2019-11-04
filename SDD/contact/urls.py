from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('feedback_results/', views.feedback_results, name='feedback_results'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('sponsor_results/', views.sponsor_results, name='sponsor_results'),
]
