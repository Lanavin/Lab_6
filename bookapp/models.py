from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, null=True)


    objects = models.Manager()
