from django.contrib import admin
from order import models
# Register your models here.

admin.site.register([models.Cart,models.Orders])