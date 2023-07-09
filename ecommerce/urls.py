from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import ProductForm,ProductsListView, CategoryListView,CategoryDetailView
from main.views import UserRegisterView
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/add',ProductForm.as_view(),name='product-add'),
    path('products/',ProductsListView.as_view(),name='product-list'),
    path('',CategoryListView.as_view(),name='category-list'),
    path('cat/<int:pk>',CategoryDetailView.as_view(),name='category-detail'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(template_name='main/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]

if settings.DEBUG == True:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

