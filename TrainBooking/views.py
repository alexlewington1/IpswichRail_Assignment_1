from django.shortcuts import render

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
