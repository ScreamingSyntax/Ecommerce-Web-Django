from django.shortcuts import render

from django.views.generic import CreateView,ListView,DetailView
from products.models import Products,Category

class ProductForm(CreateView):
    model = Products
    fields = ['name','quantity','image','category','price']

class ProductsListView(ListView):
    model = Products
    context_object_name='products'
    # template_name='products/products_display.html'

class CategoryListView(ListView):
    model = Category
    context_object_name='categories'


class CategoryDetailView(DetailView):
    model = Category
