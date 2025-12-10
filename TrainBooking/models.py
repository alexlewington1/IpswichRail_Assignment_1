from django.db import models

class LoginDetails(models.Model):
    username = models.CharField("Username", max_length=30, unique=True)
    password = models.CharField("Password", max_length=30)




