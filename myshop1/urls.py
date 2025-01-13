
"""myshop1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myshop1 import views
from rest_framework.urlpatterns import format_suffix_patterns
from .yasg import urlpatterns as doc_urls
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myshop1/users/', views.users_list, name='users_list'),
    path('myshop1/users/<int:id>/', views.users_detail),

    path('myshop1/create_user/', views.create_user),
    path('myshop1/items/', views.items_list, name='items_list'),
    path('myshop1/items/<int:id>/', views.item_detail, name='item_detail'),
    path('create_item/', views.create_item, name='create_item'),

    path('myshop1/order_items/', views.order_items_list),
    path('myshop1/order_items/<int:id>', views.order_items_detail),
    path('create_order_item/', views.create_order_item, name='create_order_item'),
    path('myshop1/users/<int:id>/orders/', views.get_user_orders, name='user_orders'),
    path('myshop1/login/', obtain_auth_token, name = "login"),
    path('myshop1/logout_user/', views.logout_user, name="logout_user"),
    path('account/', include('account.urls')),



    path('myshop1/homepage', views.homepage),
    path('myshop1/homepage1', views.homepage1),
]



urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)