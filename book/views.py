from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def show_age(request, age):
    return HttpResponse("I am %s years old." % age)
