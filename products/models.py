from django.db import models
# Create your models here.
# def Products(models)
from django.shortcuts import redirect,render
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(default='default.jpg',upload_to='products_images/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()

    def get_absolute_url(self):
        return reverse('product-list')