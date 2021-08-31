from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self) -> str:
        return self.name


class Destination:
    id: int
    name: str
    img: str
    price: int