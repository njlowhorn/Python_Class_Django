from django.db import models

# Create your models here.

class Computer(models.Model):
    manufacturer = models.TextField()
    ram = models.IntegerField()
    storage_hdd = models.IntegerField()
    storage_ssd = models.IntegerField()
    operating_system = models.TextField()
    price = models.FloatField()

class Customer(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.TextField()
    card_number = models.TextField()

class Desktop(Computer):
    has_monitor = models.BooleanField()

class Laptop(Computer):
    battery_life = models.IntegerField()


