from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'

    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name='car_models'
    )
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=20,
        choices=CAR_TYPE_CHOICES,
        default=SEDAN
    )
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023),
        ]
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"