#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<html><title>Polls site</title><h1>Hello, world. You're at the polls index.</h1></html>") #HttpResponse("<html><title>To-Do lists</title><h1>Lists</h1></html>")

