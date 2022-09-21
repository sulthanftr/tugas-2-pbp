from django.urls import path
from .views import *

app_name = 'watchlist'

urlpatterns = [
    path('html', show_mywatchlist, name='show_mywatchlist'),
    path('xml', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
]