from django.shortcuts import render
from .models import TrainTimes

def index(response):
    return render (response, 'index.html')
def availabletrains(response):
    return render (response, 'availabletrains.html')
def createaccount(response):
    return render (response, 'createaccount.html')
def login(response):
    return render (response, 'login.html')
def ticketbooking(response):
    return render (response, 'ticketbook.html')
def ticketsearch(response):
    return render (response, 'ticketsearch.html')
def available_trains(request):
    trains = TrainTimes.objects.all().order_by('departure_time')
    return render(request, "available_trains.html", {"trains": trains})