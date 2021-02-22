from django.db import models
#from django.db.models.deletion import En

# Create your models here.
from django.db.models import IntegerField


class Sort(models.Model):
    sort = models.TextField(max_length=400)
    state = models.IntegerField(default=1)


class SubSort(models.Model):
    subsort = models.TextField(max_length=400)
    sort = models.ForeignKey(Sort, on_delete=models.CASCADE,null=True)
    state = models.IntegerField(default=1)


class Cart(models.Model):
    buyer=models.TextField(max_length=200, null=True)
    seller=models.TextField(max_length=200, null=True)
    state=models.IntegerField(default=1)
    product=models.TextField(max_length=700, null=True)
    product_qentity=models.IntegerField(default=1)


class Order(models.Model):
    seller=models.TextField(max_length=200, null=True)
    buyer=models.TextField(max_length=200, null=True)
    product=models.TextField(max_length=700, null=True)
    state=models.IntegerField(default=1)
    product_qentity=models.IntegerField(default=1)


class User(models.Model):
    firstname = models.TextField(max_length=200)
    lastname = models.TextField(max_length=200 )
    username = models.TextField(max_length=200, unique=True)
    password = models.TextField(max_length=200)
    email = models.TextField(max_length=200, unique=True)
    usertype = models.IntegerField(default=1)
    state = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    address = models.TextField(max_length=400, null=True)
    phone = models.TextField(max_length=100, null=True)


class Product(models.Model):
    product_seller=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.TextField(max_length=200)
    product_price=models.FloatField(max_length=10)
    product_qentity=models.IntegerField(default=1)
    product_shortD=models.TextField(max_length=300)
    product_longD=models.TextField()
    product_img=models.ImageField(upload_to = 'polls/static/pic_folder/', default = 'polls/static/pic_folder/star.png')
    subsort = models.ForeignKey(SubSort, on_delete=models.CASCADE,null=True)
    sort = models.ForeignKey(Sort, on_delete=models.CASCADE,null=True)







