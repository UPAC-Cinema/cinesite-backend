from django.urls import path

from . import views

app_name = 'about'
urlpatterns = [
    path('bylaws/', views.bylaws, name='bylaws'),
    path('faq/', views.faq, name='faq'),
    path('policy/', views.policy, name='policy'),


]
