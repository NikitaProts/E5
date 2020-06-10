from django.db import models


class Car(models.Model):
    MECHANIC = 1
    AUTOMATIC = 2
    ROBOT = 3
    TRANSMISSION_CHOICES = [
        (MECHANIC, 'Механика'),
        (AUTOMATIC, 'Автомат'),
        (ROBOT, 'Робот')
    ]

    manufacturer = models.CharField(max_length=64, default=None)
    car_model = models.CharField(max_length=64, default=None)
    production_year = models.IntegerField(default=1900)
    transmission = models.SmallIntegerField(default=MECHANIC, choices=TRANSMISSION_CHOICES)
    car_color = models.CharField(max_length=64, default=None)

    def __str__(self):
        return self.car_model
