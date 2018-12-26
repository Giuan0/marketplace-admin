from django.db import models
from store.models import Store

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    