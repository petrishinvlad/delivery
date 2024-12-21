from django.shortcuts import render
from django.http import HttpResponse

def show_age(request, age):
    return HttpResponse("I am %s years old." % age)

def show_name(request, name):
    return HttpResponse("Hello, I am showing the name - %s" % name)

def index(request):
    my_dict = {'insert_me': "Hello I am from views.py!"}
    return render(request, 'book/index.html', context=my_dict)

def home(request):
    return render(request, 'book/home.html')

def search(request):
    return render(request, 'book/search.html')

def about(request):
    return render(request, 'book/about.html')
