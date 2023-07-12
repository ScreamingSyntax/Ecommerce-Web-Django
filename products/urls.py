from django.urls import path
from products.views import *

urlpatterns = [
    path('product/add',ProductForm.as_view(),name='product-add'),
    path('products/',ProductsListView.as_view(),name='product-list'),
    path('',CategoryListView.as_view(),name='category-list'),
    path('cat/<int:pk>',CategoryDetailView.as_view(),name='category-detail'),
    path('products/<int:pk>',ProductDetailView.as_view(),name='product-detail'),
    path('searchbar/',SearchProductView.as_view(),name='searchbar'),
    path('searchbar/cart/<int:pk>',SearchAddToCart.as_view(),name='search-cart' ),
]