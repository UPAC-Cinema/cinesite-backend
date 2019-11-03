from django.urls import path

from . import views

app_name = 'policy'
urlpatterns = [
    path('', views.index, name='index'),
]
