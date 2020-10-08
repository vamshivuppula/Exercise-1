#from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('import/', import_data, name='import'),
    path('', DataListView.as_view(), name='landing_page')
]
