from django.shortcuts import render

tasks = ["foo", "bar", "baz"] #global variable

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks #key : value pair
    })

def add(request):
    return render(request, "tasks/add.html")
    