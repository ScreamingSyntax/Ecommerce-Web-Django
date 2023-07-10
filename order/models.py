from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from django.utils import timezone

class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    user= models.ForeignKey(User,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    date = models.DateField(default=timezone.now)
