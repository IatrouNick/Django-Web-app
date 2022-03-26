from django.db import models

# Create your models here.

class Clothes(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits = 5,decimal_places = 2)

     