from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.fields import SmallIntegerField

# Create your models here.

class Inventory(models.Model):
    name                        = models.CharField(max_length=500)
    cost_price			        = models.DecimalField(verbose_name="Cost Price" ,max_digits=7, decimal_places=2)
    price			            = models.DecimalField(max_digits=7, decimal_places=2)
    quantity                    = models.SmallIntegerField()
    timestamp  		            = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name                        = models.CharField(max_length=500)
    price			            = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp  		            = models.DateField(auto_now_add=True)
    quantity                    = SmallIntegerField(validators = [MinValueValidator(0)])
    timestamp  		            = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Sales(models.Model):
    product                     = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity                    = SmallIntegerField(validators = [MinValueValidator(1)])
    price			            = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp  		            = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name