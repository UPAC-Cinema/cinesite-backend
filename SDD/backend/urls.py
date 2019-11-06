from django.urls import path

from . import views

app_name = 'backend'
urlpatterns = [
    path('', views.officers, name='officers'),
    path('update_sched/', views.update_sched, name='update_sched')
]
