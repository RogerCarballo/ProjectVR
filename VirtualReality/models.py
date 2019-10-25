from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    class Meta:
        verbose_name_plural= "Room"
    capacity = models.IntegerField()
    location = models.CharField(max_length=200)
    glasses_availables = models.IntegerField();

class Glasses(models.Model):
    class Meta:
        verbose_name_plural= "Glass"
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    glasses_model = models.CharField(max_length=200)



class Reservation(models.Model):
    class Meta:
        verbose_name_plural= "Reservation"
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    init_hour = models.DateTimeField()
    final_hour = models.DateTimeField()
    num_persons = models.IntegerField()
    glasses = models.ManyToManyField(Glasses)

