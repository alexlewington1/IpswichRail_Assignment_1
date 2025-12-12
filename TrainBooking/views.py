from django.shortcuts import render
from .models import TrainTime

def index(response):
    return render (response, 'index.html')
def createaccount(response):
    return render (response, 'createaccount.html')
def login(response):
    return render (response, 'login.html')
def ticketbooking(response):
    return render (response, 'ticketbook.html')
def ticketsearch(response):
    return render (response, 'ticketsearch.html')
def available_trains(request):
    # Get filter parameter
    selected_station = request.GET.get('station')

    # Get all unique departure stations for the dropdown
    stations = TrainTime.objects.values_list('departure_station', flat=True).distinct()

    # Filter trains if a station is selected
    if selected_station:
        trains = TrainTime.objects.filter(departure_station=selected_station).order_by('departure_time')
    else:
        trains = TrainTime.objects.all().order_by('departure_time')

    return render(request, "available_trains.html", {
        "trains": trains,
        "stations": stations,
        "selected_station": selected_station
    })

