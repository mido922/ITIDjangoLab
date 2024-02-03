from django.db import models

# Create your models here.

class Product(models.Model):
    ID = models.CharField(max_length=30)
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=50)
    Category = models.CharField(max_length=30)