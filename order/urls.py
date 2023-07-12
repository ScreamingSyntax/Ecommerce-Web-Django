from django.urls import path
from order.views import *

urlpatterns = [
    path('cart/',CartView.as_view(),name='cart'),
    path('cart/del/<int:pk>',DeleteCart.as_view(),name='delete-cart'),
    path('cart/inc/<int:pk>',IncrementCart.as_view(),name='increment-cart'),
    path('cart/dec/<int:pk>',DecrementCart.as_view(),name='decrement-cart'),
    path('status/',OrderStatus.as_view(),name='status'),
    path('checkout/',OrderCheckoutForm.as_view(),name='checkout'),
]