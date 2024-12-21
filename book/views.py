from django.shortcuts import render
from django.http import HttpResponse

def show_age(request, age):
    return HttpResponse("I am %s years old." % age)

def index(request):
    my_dict = {'insert_me': "Hello I am from views.py!"}
    return render(request, 'book/index.html', context=my_dict)
