from django.db import models

# Create your models here.
class Expense(models.Model):
    name                        = models.CharField(max_length=500)
    description                 = models.CharField(max_length=2000, null=True, blank=True)
    amount                      = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp  		            = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name