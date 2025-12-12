from django.db import models

class LoginDetails(models.Model):
    username = models.CharField("Username", max_length=30, unique=True)
    password = models.CharField("Password", max_length=30)

class TrainTime(models.Model):
    departure_time = models.TimeField()
    departure_station = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    arrival_station = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f"{self.departure_station} -> {self.arrival_station}"
