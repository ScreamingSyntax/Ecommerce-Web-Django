from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import ProductForm,ProductsListView, CategoryListView,CategoryDetailView,ProductDetailView,SearchProductView,SearchAddToCart
from main.views import UserRegisterView
from django.contrib.auth.views import LoginView,LogoutView
from order.views import CartView,DeleteCart,IncrementCart,DecrementCart
# from order.views import 
from order.views import OrderCheckoutForm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/add',ProductForm.as_view(),name='product-add'),
    path('products/',ProductsListView.as_view(),name='product-list'),
    path('',CategoryListView.as_view(),name='category-list'),
    path('cat/<int:pk>',CategoryDetailView.as_view(),name='category-detail'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(template_name='main/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('cart/',CartView.as_view(),name='cart'),
    path('products/<int:pk>',ProductDetailView.as_view(),name='product-detail'),
    path('cart/del/<int:pk>',DeleteCart.as_view(),name='delete-cart'),
    path('cart/inc/<int:pk>',IncrementCart.as_view(),name='increment-cart'),
    path('cart/dec/<int:pk>',DecrementCart.as_view(),name='decrement-cart'),
    path('searchbar/',SearchProductView.as_view(),name='searchbar'),
    path('searchbar/cart/<int:pk>',SearchAddToCart.as_view(),name='search-cart' ),
    path('checkout/',OrderCheckoutForm.as_view(),name='checkout'),
    # path('orders/',OrderCustomerView.as_view(),name='orders')
]

if settings.DEBUG == True:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

