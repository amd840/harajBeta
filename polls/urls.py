"""kfupmharaj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path

from . import views
from .templatetags import index

app_name = 'polls'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('ss/', views.signups, name="signups"),
    path('login/', views.login, name="login"),
    path('search/', views.search, name="search"),

    
    path('addproduct/', views.addproduct, name="addproduct"),
    #path('upload_pic/', views.upload_pic, name="upload_pic"),
    path('panel/<str:orderid>/', views.panel, name="panel"),
    path('order/', views.order, name="order"),
    path('lang/', index.setLang, name="lang"),

    path('orderCompletion/<int:orderid>/', views.orderCompletion, name="orderCompletion"),


    path('addproduct/<int:productid>/', views.addToCart, name="addToCart"),
    path('decproCount/<int:productid>/', views.decPro, name="decPro"),

    path('editproduct/<int:productid>/', views.editProduct, name="editProduct"),
    path('saveEditP/<int:productid>/', views.saveEditP, name="saveEditP"),

    path('logout/', views.logout, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('delcart/<int:cartId>', views.delCart, name="delCart"),
    path('makeOrder/', views.makeOrder, name="makeOrder"),
    path('product/<int:productid>/', views.product, name="product"),
    path('deleteProduct/<int:productid>/', views.deleteProduct, name="deleteProduct"),



]
