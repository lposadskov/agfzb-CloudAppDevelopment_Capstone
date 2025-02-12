from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=1000)
    est_date = models.DateField(null=True)
    est_country = models.CharField(max_length=30)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description


# Car Model model
class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    CAR_TYPE = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]
    maker = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealerid = models.IntegerField(default=0)
    name = models.CharField(null=False, max_length=30)
    type = models.CharField(max_length=5, choices=CAR_TYPE, default=SEDAN)
    year = models.DateField(null=True)

    def __str__(self):
        return "Name: " + self.name


class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, st, state, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer state
        self.st = st
        self.state = state
        # Dealer zip
        self.zip = zip

    def __str__(self):
        #return "Address: " + self.address
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = ""
        self.id = id

    def __str__(self):
        #return "Address: " + self.address
        return "Dealership: " + self.dealership