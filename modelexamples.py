from django.db import models

class AppUser(models.Model):
    account_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(unique=True)
    password = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    street_name = models.TextField()
    street_number = models.TextField()
    zip_code = models.TextField()
    city = models.TextField()
    
    def __str__(self):
        return f"Profile for {self.account_id}"

class CarModel(models.Model):
    car_model_id = models.AutoField(primary_key=True)
    make = models.TextField()
    model = models.TextField(unique=True)
    
    def __str__(self):
        return f"{self.make} {self.model}"

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    number_of_owners = models.PositiveIntegerField()
    registration_number = models.TextField(unique=True)
    manufacture_year = models.PositiveIntegerField()
    number_of_doors = models.PositiveIntegerField(default=5)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    mileage = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.car_model} ({self.registration_number})"

class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)
    advertisement_date = models.DateTimeField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    seller_account = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Ad for {self.car} by {self.seller_account}"
