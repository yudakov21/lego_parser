from django.db import models

# Create your models here.
class LegoToy(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=10, null = True, blank = True)
    pieces = models.IntegerField(null = True, blank = True)
    rating = models.FloatField(null = True, blank = True)
    price = models.CharField(max_length=50, null = True, blank = True)
    discount = models.CharField(max_length=50, null = True, blank = True)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name