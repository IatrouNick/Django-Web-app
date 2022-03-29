from django.db import models
from django.templatetags.static import static

# Create your models here.

class Clothes(models.Model):
    TYPE_CHOICES = [
        ('Hats','H'),
        ('Dresses', 'D'),
        ('Shoes', 'S'),
        ('Bags', 'B'),
    ]
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50)
    typeCloth = models.CharField(max_length=50, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits = 5,decimal_places = 2)

    @property
    def img_url(self):
        return static("images/{}.jpg".format(self.type))
     