from django.db import models
from products.models import Products
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    sub_total = models.IntegerField(default=1)
    def save(self,*args,**kwargs):
        self.sub_total=self.quantity*self.product.price
        # im
        super().save(*args,**kwargs)
    def __str__(self):
        return self.user

ORDER_STATUS = (
  ("Order Processing", "Order Processing"),
  ('Order Recieved', "Order Recieved"),
  ("On The Way", "On the Way"),
  ("Order completed", "Order completed"),
)
class OrderItem(models.Model):
    order = models.ForeignKey('Orders', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(default=ORDER_STATUS[0][0], max_length=250, choices=ORDER_STATUS, null=True)
    def __str__(self):
        return f"{self.order} - {self.product}"

class Orders(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    shipping_address = models.CharField(max_length=50)
    user_city = models.CharField(max_length=50)
    user_mobile = models.IntegerField()
    final_amount = models.PositiveIntegerField(default=0)
   
    
    def get_absolute_url(self):
        return reverse('cart')
    
    def __str__(self):
        return f"${self.user} {self.date}"