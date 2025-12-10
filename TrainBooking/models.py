from django.db import models

class LoginDetails(models.Model):
    username = models.CharField("Username", max_length=30, unique=True)
    password = models.CharField("Password", max_length=30)

class TrainTimes(models.Model):
    departure_station = models.CharField("Departure Station", max_length=30)
    arrival_station = models.CharField("Arrival Station", max_length=30)
    arrival_time = models.CharField("Arrival Time", max_length=30)
    departure_time = models.CharField("Departure Time", max_length=30)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)



