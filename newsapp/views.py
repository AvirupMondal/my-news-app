from django.http import request
from django.shortcuts import render
from newsapi import NewsApiClient
import requests
# Create your views here.
def index(request):
    return render(request, 'index.html')

def newsBusinessFetch(request):
    
    url=f'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=227b5154fda140acbe037bc79ba4555b'
    response=requests.get(url)
    data=response.json()
    articles=data['articles']  
    context={'response': articles}                      
    return render(request, 'business.html',context)
def newsScienceFetch(request):
    
    url=f'https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=227b5154fda140acbe037bc79ba4555b'
    response=requests.get(url)
    data=response.json()
    articles=data['articles']  
    context={'response': articles}                      
    return render(request, 'science.html',context)
def newsSportsFetch(request):
    
    url=f'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=227b5154fda140acbe037bc79ba4555b'
    response=requests.get(url)
    data=response.json()
    articles=data['articles']  
    context={'response': articles}                      
    return render(request, 'sports.html',context)
def newsTechnologyFetch(request):
    
    url=f'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=227b5154fda140acbe037bc79ba4555b'
    response=requests.get(url)
    data=response.json()
    articles=data['articles']  
    context={'response': articles}                      
    return render(request, 'technology.html',context)
def newsHealthFetch(request):
    
    url=f'https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=227b5154fda140acbe037bc79ba4555b'
    response=requests.get(url)
    data=response.json()
    articles=data['articles']  
    context={'response': articles}                      
    return render(request, 'health.html',context)
