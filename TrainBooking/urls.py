from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("availabletrains/", views.available_trains, name="availabletrains"),
path("createaccount/", views.createaccount, name="createaccount"),
path("login/", views.login, name="login"),
path("ticketbooking/", views.ticketbooking, name="ticketbook"),
path("ticketsearch/", views.ticketsearch, name="ticketsearch"),
path("bookingconfirmation/", views.bookingconfirmation, name="bookingconfirmation"),


]