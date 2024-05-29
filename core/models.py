from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - ${self.amount}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Carrier(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicleType = models.CharField(max_length=50)
    carPatent = models.CharField(max_length=10)
    vehicleModel = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicleModel
