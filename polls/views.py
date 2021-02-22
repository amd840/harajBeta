from django import forms
from django.db import models

from django.shortcuts import render
from django.core import serializers
import json
from collections import namedtuple

# Create your views here.
from django.http import HttpRequest, HttpResponseForbidden

from django.http import HttpResponse, HttpRequest,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Cart, User, Product, Order, Sort, SubSort
from django.template import loader
from django.contrib.sessions.backends.db import SessionStore as DBStore
from django.contrib.sessions.base_session import AbstractBaseSession

def index(request):
    products = Product.objects.order_by('id')
    imagelist = []
    for pro in products:
        imagelist.append(pro.product_img.name[5:])
    # return HttpResponse(imagelist)
    if (request.session.get('theuser')):
        euser = User.objects.get(username=request.session.get('theuser'))
        return render(request, 'polls/index.html', {'product': products, 'theuser': euser, "imgs": imagelist})

    return render(request, 'polls/index.html', {'product': products, "imgs": imagelist})

    return HttpResponse("Home Page")


def signup(request):
    # users = User.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/signup.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse('polls/signup.html')

    if (request.POST):
        user = User(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                    username=request.POST['username'], email=request.POST['email'], password=request.POST['password'],address=request.POST['address'], phone=request.POST['phone'])
        user.save()
        request.session['seller'] = user.username
        request.session['theuser'] = user.username
        return HttpResponseRedirect('/')
        # return index(request)

    else:
        return render(request, 'polls/signup.html')


def signups(request):
    user = User(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])

    user.save()

    return render(request, 'polls/signups.html', {'user': user})


def login(request):
    if (request.POST):
        user = get_object_or_404(User, username=request.POST['username'])
        if (user.password == request.POST['password']):
            request.session['seller'] = user.username
            request.session['theuser'] = user.username
            if((request.session.get('cart'))):
                addCartToUser(request, user)

            # return render(request, 'polls/addproduct.html')
            return HttpResponseRedirect('/')
            return index(request)
        else:
            return HttpResponse("wrong password")
    else:
        return render(request, 'polls/login.html')


def addCartToUser(request,user):
    data = (request.session.get('cart'))
    for x in data:
        cart = Cart(product=x["fields"]["product"], buyer=user.username, seller=x["fields"]["seller"], state=x["fields"]["state"],
                    product_qentity=x["fields"]["product_qentity"])
        cart.save()



def product(request,productid):
    product = Product.objects.get(pk=productid)

    return render(request, 'polls/product.html',{'product':product})


def addproduct(request):

    seller = get_object_or_404(User, username=request.session['seller'])
    sorts = Sort.objects.all()
    subsorts = SubSort.objects.all()
    if (request.POST):
        psort = SubSort.objects.get(pk=request.POST['sort'])


        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(
                product_seller=seller,
                product_name=request.POST['product_name'],
                              product_price=request.POST['product_price'],
                              product_qentity=request.POST['product_qentity'],
                              product_shortD=request.POST['product_shortD'],
                              product_longD=request.POST['product_longD'],

                              sort = psort.sort,
                            subsort = psort

            )
            product.product_img = form.cleaned_data['image']
            product.save()
            return HttpResponseRedirect('/')

            # return index(request)

    return render(request, 'polls/addproduct.html',{'sorts':sorts,'subsorts':subsorts})

def decPro(request, productid):
    product = Product.objects.get(pk=productid)
    seller = product.product_seller
    if (product.product_qentity > 0):

        if (request.session.get('theuser')):
            buyer = User.objects.get(username=request.session['theuser'])
            # return HttpResponse(buyer)
            # if(len(buyer.cart_set.all)>0):
            # return HttpResponse(buyer.order)
            try:

                cart = Cart.objects.filter(product=productid, buyer=buyer.username, state=1).get(product=productid)
                if (cart.product_qentity > 1):
                    cart.product_qentity -= 1
                    cart.save()
                else:
                    return delCart(request, cart.id)

            except (KeyError, Cart.DoesNotExist):
                cart = Cart(product=productid, buyer=buyer.username, seller=seller.username, state=1, product_qentity=1)
                cart.save()

            return HttpResponseRedirect('/')

            buyer = request.session['theuser']
            # return HttpResponse(product.product_seller)
            seller = product.product_seller

            # order = Order(product=product, buyer=buyer, seller=seller, state=1, product_qentity=1)
            # order.save()
        elif (request.session.get('cart')):
            # del request.session['cart']
            # return HttpResponseRedirect('/')
            cart = Cart(product=productid, buyer="", seller=seller.username, state=1, product_qentity=1)
            data = (request.session.get('cart'))

            for x in data:
                if x["fields"]["product"] == cart.product:
                    x["fields"]["product_qentity"] -= 1
                    request.session['cart'] = data
                    return HttpResponseRedirect('/')

            # data.append()
            # str = type(data)
            # return HttpResponse(data)
            cartcvalue = {'model': 'polls.cart', 'pk': len(data),
                          'fields': {'buyer': '', 'seller': cart.seller, 'state': cart.state, 'product': cart.product,
                                     'product_qentity': cart.product_qentity}}

            data.append(cartcvalue)
            # return HttpResponse(str(data))

            # carts.append(cart)
            # del request.session['cart']
            dataw = str(data)
            dataw = dataw.replace("'", '"')
            dataw = json.dumps(data)
            # return HttpResponse((dataw))

            # dataw = dataw.replace("'", '"')

            request.session['cart'] = json.loads(dataw)
            # request.session['cart'] = serializers.serialize('json', data)
    else:
        return HttpResponseRedirect('/')


def addToCart(request, productid):
    product = Product.objects.get(pk=productid)
    seller = product.product_seller
    if(product.product_qentity>0):

        if (request.session.get('theuser')):
            buyer = User.objects.get(username=request.session['theuser'])
            # return HttpResponse(buyer)
            # if(len(buyer.cart_set.all)>0):
            # return HttpResponse(buyer.order)
            try:
                cart = Cart.objects.filter(product=productid, buyer=buyer.username , state=1).get(product=productid)
                cart.product_qentity += 1
                cart.save()

            except (KeyError, Cart.DoesNotExist):
                cart = Cart(product=productid, buyer=buyer.username, seller=seller.username, state=1, product_qentity=1)
                cart.save()


            return HttpResponseRedirect('/')

            buyer = request.session['theuser']
            # return HttpResponse(product.product_seller)
            seller = product.product_seller

            # order = Order(product=product, buyer=buyer, seller=seller, state=1, product_qentity=1)
            # order.save()
        elif (request.session.get('cart')):
            # del request.session['cart']
            # return HttpResponseRedirect('/')
            cart = Cart(product=productid, buyer="", seller=seller.username, state=1, product_qentity=1)
            data = (request.session.get('cart'))

            for x in data:
                if x["fields"]["product"] == cart.product:
                    x["fields"]["product_qentity"]+=1
                    request.session['cart'] = data
                    return HttpResponseRedirect('/')


            # data.append()
            # str = type(data)
            # return HttpResponse(data)
            cartcvalue = {'model': 'polls.cart', 'pk': len(data), 'fields': {'buyer': '', 'seller': cart.seller, 'state': cart.state, 'product': cart.product, 'product_qentity': cart.product_qentity}}

            data.append(cartcvalue)
            # return HttpResponse(str(data))

            # carts.append(cart)
            # del request.session['cart']
            dataw = str(data)
            dataw = dataw.replace("'",'"')
            dataw = json.dumps(data)
            # return HttpResponse((dataw))

            # dataw = dataw.replace("'", '"')

            request.session['cart'] = json.loads(dataw)
            # request.session['cart'] = serializers.serialize('json', data)



    else:
        cart = Cart(product=productid, buyer="", seller=seller.username, state=1, product_qentity=1)
        cart.id = 0
        # return HttpResponse(cart.id)
        carts = []
        carts.append(cart)
        # return HttpResponse(json.loads(serializers.serialize('json', carts)))

        cartcvalue = {'model': 'polls.cart', 'pk': 0, 'fields': {'buyer': '', 'seller': seller.username, 'state': 1, 'product': productid, 'product_qentity': 1}}


        # return HttpResponse(carts)


        request.session['cart'] =  json.loads(serializers.serialize('json', carts))
    return HttpResponseRedirect('/')



    # return index(request)

    # cart = Cart(product_seller.)


def logout(request):
    request.session['seller'] = ''

    request.session['theuser'] = ''
    # return index(request)
    return HttpResponseRedirect('/')



def cart(request):
    # products = user.cart_set.all()
    if (request.session.get('theuser')):
        user = User.objects.get(username=request.session['theuser'])
        carts = Cart.objects.filter(buyer=user.username,state=1)
        return render(request, 'polls/cart.html', {'carts': carts, 'user': user})
    if (request.session.get('cart')):

        carts2 = (request.session.get('cart'))
        # carts2.count
        # return HttpResponse((carts2))

        cartlist = []
        for x in carts2:
            cart = Cart(product=x["fields"]["product"], buyer="", seller=x["fields"]["seller"], state=x["fields"]["state"], product_qentity=x["fields"]["product_qentity"],pk=x["pk"])
            cartlist.append(cart)


        return render(request, 'polls/cart.html', {'carts': cartlist})
    # return HttpResponse(carts)
    return render(request, 'polls/cart.html')


def makeOrder(request):
    if (request.session.get('theuser')):
        user = User.objects.get(username=request.session['theuser'])


        carts = Cart.objects.filter(buyer=user.username, state=1)
        for cart in carts:
            product = Product.objects.get(pk=cart.product)
            if(product.product_qentity>=cart.product_qentity):
                cart.state = 2
                cart.save()
                order = Order(product=cart.product, seller=cart.seller, buyer=cart.buyer, state=1, product_qentity=cart.product_qentity)

                order.save()
                product.product_qentity -= cart.product_qentity
                product.save()
    return HttpResponseRedirect('/cart')




def delCart(request, cartId):
    if (request.session.get('theuser')):
        mycart = Cart.objects.get(pk=cartId)
        mycart.delete()

        return cart(request)
    else:
        carts = (request.session.get('cart'))
        # return HttpResponse(carts)
        carts.pop(cartId)
        request.session['cart'] = carts
        return cart(request)


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


def panel(request,orderid):
    if (request.session.get('theuser')):
        euser = User.objects.get(username=request.session.get('theuser'))
        order = Order.objects.filter(seller=euser.username)
    return render(request, 'polls/panal.html',{'username':euser,'orders':order,'page':orderid})


def order(request):
    if (request.session.get('theuser')):
        euser = User.objects.get(username=request.session.get('theuser'))
        orders = Order.objects.filter(seller=euser.username)

    return render(request, 'polls/order.html',{'username':euser,'orders':orders})


def orderCompletion(request,orderid):
    if (request.session.get('theuser')):
        euser = User.objects.get(username=request.session.get('theuser'))

        order = euser.order_set.get(pk=orderid)
        order.state = 2
        order.save()

        return HttpResponseRedirect('/order')


def editProduct(request,productid):
    product = Product.objects.get(pk=productid)
    euser = User.objects.get(username=request.session.get('theuser'))
    sorts = Sort.objects.all()
    subsorts = SubSort.objects.all()

    if(product.product_seller == euser):
        return render(request, 'polls/addproduct.html',{'product':product, 'sorts':sorts,'subsorts':subsorts})
    else:
        return HttpResponseRedirect('/')
        return index(request)


def saveEditP(request,productid):
    product = Product.objects.get(pk=productid)
    euser = User.objects.get(username=request.session.get('theuser'))
    if (request.POST):
        form = ImageUploadForm(request.POST, request.FILES)
        product.product_name=request.POST['product_name']
        product.product_price=request.POST['product_price']
        product.product_qentity=request.POST['product_qentity']
        product.product_shortD=request.POST['product_shortD']
        product.product_longD=request.POST['product_longD']
        sort = SubSort.objects.get(pk=request.POST['sorts'])

        product.sort= sort.sort
        product.subsort=sort

        if form.is_valid():
            product.product_img=form.cleaned_data['image']
        product.save()
    # return index(request)
        return HttpResponseRedirect('/')
    return HttpResponse("no post req")



def deleteProduct(request,productid):
    product = Product.objects.get(pk=productid)
    euser = User.objects.get(username=request.session.get('theuser'))
    if (product.product_seller == euser):
        product.delete()
    return HttpResponseRedirect('/')






# class myProduct(models.Model):
#     product_img = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
#

# def upload_pic(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             m = ExampleModel.objects.get(pk=course_id)
#             m.model_pic = form.cleaned_data['image']
#             m.save()
#             return HttpResponse('image upload success')
#     return HttpResponseForbidden('allowed only via POST')
