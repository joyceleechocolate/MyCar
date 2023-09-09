from django.db import models

# Create your models here.
class CarModel(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

class Car(models.Model):
    car_model_id = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    number_of_owners = models.IntegerField(default=0)
    registration_number = models.CharField(max_length=255)
    manufacture_year = models.IntegerField()
    number_of_doors = models.IntegerField()
    mileage = models.IntegerField()

class AppUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class UserProfile(models.Model):
    account_id = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Advertisement(models.Model):
    advertisement_date = models.DateTimeField()
    seller_account_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)

