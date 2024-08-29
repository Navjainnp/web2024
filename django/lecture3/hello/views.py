from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): #index is function & request is argument-represents http request that the user made to access web serve. 
    return HttpResponse("hello, world!")

def navjain(request):
    return HttpResponse("hello Nav Jain")

def greet(request, name):
    return HttpResponse(f"hello, {name.capitalize()}")