from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from main import urls as user_urls
from order import urls as order_urls
from products import urls as product_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(product_urls),name='home'),
    path('user/',include(user_urls),name='user'),
    path('order/',include(order_urls),name='order'),
]

if settings.DEBUG == True:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

