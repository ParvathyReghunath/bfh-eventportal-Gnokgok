from django.shortcuts import render
from .models import Event

def index(request):

    event1 = Event()
    return render(request, "index.html",{'event1': event1})

