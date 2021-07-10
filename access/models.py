from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    
