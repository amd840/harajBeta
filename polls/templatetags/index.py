from django import template
from polls.models import Cart, User, Product, Order, Sort, SubSort

register = template.Library()


@register.filter
def index(indexable, i):
    if len(indexable) > i-1:
        if indexable[i-1]:
            return indexable[i-1]
    else:
        return "static/pic_folder/star.png"


@register.filter
def getImgUrl(url):
    if(url):
        return url[5:]
    else:
        return "/static/pic_folder/star.png"


@register.filter
def orderStat(st):
    if(st==1):
        return "processing"
    elif(st==2):
        return "completed"


@register.filter
def getCartPro(cart,val):
    product = Product.objects.get(pk=cart.product)
    if(val=="name"):
        return product.product_name
    elif(val=="price"):
        return product.product_price
    elif (val == "qu"):
        return cart.product_qentity
    elif (val == "short"):
        return product.product_shortD
    elif (val == "long"):
        return product.product_longD
    elif (val == "id"):
        return int(product.pk)
    elif (val == "img"):
        imgi = product.product_img.name
        if (imgi):
            return imgi[5:]
        else:
            return "/static/pic_folder/star.png"
    return product

@register.filter
def getorder(order,val):
    product = Product.objects.get(pk=order.product)
    user = User.objects.get(username=order.buyer)
    if (val == "name"):
        return product.product_name
    elif (val == "price"):
        return product.product_price
    elif (val == "qu"):
        return product.product_qentity
    elif (val == "short"):
        return product.product_shortD
    elif (val == "long"):
        return product.product_longD
    elif (val == "state"):
        return order.state
    elif (val == "buyer"):
        return order.buyer
    elif (val == "address"):
        return user.address
    elif (val == "phone"):
        return user.phone
    elif (val == "img"):

        imgi = product.product_img.name
        if (imgi):
            return imgi[5:]
        else:
            return "/static/pic_folder/star.png"
    return product

@register.filter
def panalPage(page):
    return (page == "OrderTobeShipped")


@register.filter
def plus(plus):
    # cart.product_qentity+=1
    cart1 = Cart.objects.get(pk=8)
    cart1.seller = "alii"
    cart1.save()






# < img src = "{% static 'img.png' %}" >
