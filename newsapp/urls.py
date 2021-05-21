
from django.contrib import admin
from django.urls import path, include
from newsapp import views

urlpatterns = [
    path('business', views.newsBusinessFetch, name='newsBusinessFetch'),
    path('science', views.newsScienceFetch, name='newsScienceFetch'),
    path('', views.newsHealthFetch, name='newsHealthFetch'),
    path('sports', views.newsSportsFetch, name='newsSportsFetch'),
    path('technology', views.newsTechnologyFetch, name='newsTechnologyFetch'),
    
]
