import datetime

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "newyear/index.html", {
        "newyear": now.manth == 1 and now.day == 1
    })