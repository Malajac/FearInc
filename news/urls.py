from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('test/', test),
    path('api/news', get_news)
]