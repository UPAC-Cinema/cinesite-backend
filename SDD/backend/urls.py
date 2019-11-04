from django.urls import path

from . import views

app_name = 'backend'
urlpatterns = [
    path('officers', views.officers, name='officers'),
]
