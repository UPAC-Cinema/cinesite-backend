'''SDD URL Configuration

    The `urlpatterns` list routes URLs to views. For more information, please see:
        https://docs.djangoproject.com/en/2.2/topics/http/urls/

    Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')

    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''
from django.urls import path, include


'''
    We have four apps that deal with pages of similar nature.

    About: contains views for the pages that simply display PDFs

    Contact: contains views for the pages that allows the user to contact the
        club via forms that send email upon correct completion.

    Backend: contains the view that allows officers to change the schedule,
        update PDFs, edit attendance, or delete movies from the schedule.

    Schedule: contains views for the homepage and the past_showings page.
'''
urlpatterns = [
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('backend/',include('backend.urls')),
    path('', include('schedule.urls')),
]
