from django.db import models

# Create the Django ORMs for main tables so that the data can always be manages by Django Admin and easy add/delete functionality


class vehicle_listings(models.Model):
    vehicle_live_id = models.IntegerField(null=True)
    vin = models.CharField(max_length=20, null=True)
    stock = models.CharField(max_length=20, null=True)
    make = models.CharField(max_length=20, null=True)
    model = models.CharField(max_length=80, null=True)
    trim = models.CharField(max_length=80, null=True)
    year = models.IntegerField(null=True)
    amenities = models.TextField(null=True)
    price = models.FloatField(null=True)
    miles = models.IntegerField(null=True)
    exterior = models.CharField(max_length=80, null=True)
    description = models.TextField(null=True)
    certified = models.IntegerField(null=True)
    transmission = models.CharField(max_length=10, null=True)
    body_type = models.CharField(max_length=50, null=True)
    doors = models.FloatField(null=True)
    cylinders = models.IntegerField(null=True)
    engine = models.CharField(max_length=80, null=True)
    displacement = models.FloatField(null=True)
    zip_code = models.CharField(max_length=10, null=False)
    imagefile = models.TextField(null=True)
    dealer_number = models.IntegerField(null=False)
    Distance = models.FloatField(null=True)


class dealers(models.Model):
    dealer_number = models.CharField(max_length=20)
    dealer_name = models.CharField(max_length=100)
    dealer_address = models.CharField(max_length=100, null=True)


class zipInfo(models.Model):
    zip_code = models.CharField(max_length=10)
    state_code = models.CharField(max_length=5)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
