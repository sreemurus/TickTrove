from django.db import models


# Create your models here.
# customers/models.py


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    building_details = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name
