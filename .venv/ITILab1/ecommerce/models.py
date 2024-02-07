from django.db import models

# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=30)
    Description = models.CharField(max_length=50)
    Category = models.CharField(max_length=10)
    Image = models.ImageField(upload_to='ecommerce/images/', blank=True, null=True)