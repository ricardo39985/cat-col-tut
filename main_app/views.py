from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from main_app import models

# Create your views here.
def home(request):
      return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    return(render(request, 'cats/index.html'))
