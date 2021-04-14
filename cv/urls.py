from django.contrib import admin
from django.urls import path
from . import views
from .views import ResumeView, ContactView

urlpatterns = [
    path('', views.home, name='cv-home'),
    path('resume', ResumeView.as_view(), name='cv-resume'),
    path('contacts', ContactView.as_view(), name='cv-contacts')
]
