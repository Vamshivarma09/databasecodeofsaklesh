from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sellar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(null=False,max_length=500)


class ProductCategory(models.Model):
    title = models.CharField(null=False,max_length=500)
    details = models.TextField(null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(null=False,max_length=500)
    details = models.TextField(null=True)
    price = models.FloatField(null=False)

    def __str__(self):
        return self.title