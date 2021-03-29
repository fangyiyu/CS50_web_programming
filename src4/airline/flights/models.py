from django.db import models

# Create your models here, and outline what data to store in the application
# Create a model that extends Django's model class, and add two charfields which only store strings.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    # Provide instructions for how to turn an Airport object into a string
    def __str__(self):
        return f"{self.city} ({self.code})"

# origin and destination are Foreign Keys because they refer to another object (Airport)
class Flight(models.Model):

    #CASCADE means that when an airport is deleted, all flights associated with it should also be deleted
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    
    # passengers have a Many to Many relationship with flights, and the first argument here is the class of objects that this one is
    # related to, blank=True means a passenger can have no flights.
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"