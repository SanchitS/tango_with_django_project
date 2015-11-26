from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says Hello to the world! <br/> <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says this is our ABOUT page ! <br/> <br/> <a href='/rango'>Main Page</a> ")