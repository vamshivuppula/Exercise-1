#from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('import/', import_data, name='signup'),
    #path('test/', test, name='signup'),
    #path('', LandingPage.as_view(), name='landing_page')
]
