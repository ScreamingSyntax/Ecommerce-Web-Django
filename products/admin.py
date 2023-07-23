from django.contrib import admin
from products import models
# Register your models here

admin.site.register([models.Category,models.Products])