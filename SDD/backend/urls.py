from django.urls import path

from . import views

app_name = 'backend'
urlpatterns = [
    path('', views.officers, name='officers'),
    path('update_sched/', views.update_sched, name='update_sched'),
    path('delete/', views.delete, name='delete'),
    path('edit/', views.edit, name='edit'),
    path('bylaws/', views.bylaws, name='bylaws'),
    path('policies/', views.policies, name='policies'),
    path('faqs/', views.faqs, name='faqs'),
]
