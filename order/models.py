from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from django.utils import timezone

class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    sub_total = models.IntegerField(default=1)
    def save(self,*args,**kwargs):
        self.sub_total=self.quantity*self.product.price
        # im
        super().save(*args,**kwargs)

class Order(models.Model):
    user_cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    shipping_address= models.CharField(max_length=50)
    user_city = models.CharField(max_length=50)
    user_mobile = models.CharField(max_length=50)
    final_amount = models.PositiveIntegerField(default=0)