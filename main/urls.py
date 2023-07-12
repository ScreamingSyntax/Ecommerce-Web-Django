from django.urls import path
from main.views import UserRegisterView,profile
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('profile/',profile,name='profile'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(template_name='main/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]
