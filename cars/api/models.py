from django.db import models

# Create your models here.

class car_details(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
    ]

    company=models.CharField(max_length=50,null=False,blank=False)
    model=models.CharField(max_length=50,null=False,blank=False)
    year_of_registration=models.DateField()
    number_of_owners=models.IntegerField(null=False,blank=False)
    total_km=models.IntegerField(null=False,blank=False)
    fuel_type=models.CharField(max_length=10, choices=FUEL_CHOICES,null=False,blank=False)
    car_image=models.ImageField(null=False,blank=False)
    car_video=models.FileField(null=True,blank=True)


    def __str__(self):
        return self.model
