from django.db import models
# Create your models here.
# def Products(models)
from django.shortcuts import redirect,render
from django.urls import reverse
from django.utils import timezone
from PIL import Image

class Category(models.Model):
    image= models.ImageField(default='default.jpg',upload_to='categories_pics/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        super().save()
        img = Image.open(self.image.path)
        if(img.height>300 or img.width>300):
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Products(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    sub_title = models.CharField(max_length=100)
    description=models.TextField()
    image = models.ImageField(default='default.jpg',upload_to='products_images/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    date_added=models.DateTimeField(default=timezone.now)   
    viwed_times = models.IntegerField(null=True,default=0)
    sold_times = models.IntegerField(null=True,default=0)
        
    def get_absolute_url(self):
        return reverse('product-add')
    
    def __str__(self):
        return self.name