import datetime
# type python and hit enter in terminal will give access to use python(modules) outside django.

from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day ==1
        #"newyear": true says YES.
    })

