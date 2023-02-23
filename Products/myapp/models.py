from django.db import models

# Create your models here.

class product_mst(models.Model):
    productname=models.CharField(max_length=50)

def __str__(self):
    return self.productname