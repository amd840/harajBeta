from django import template
from polls.models import Cart, User, Product, Order, Sort, SubSort
from django.http import HttpResponse, HttpResponseForbidden , HttpResponseRedirect

register = template.Library()


totalPrice = 0.0
lang = 'ar'
imgCounter = 0
@register.filter
def index(indexable):
    global imgCounter
    imgCounter+=1
    if len(indexable) > imgCounter-1:
        return indexable[imgCounter-1]
    else:
        return "static/pic_folder/star.png"

@register.filter
def getTitle(lst):
    return lst.first().sort.sort

@register.filter
def zeroImgIndx(zero):
    global imgCounter
    imgCounter = 0
    return ''

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
        global totalPrice
        totalPrice+=float(product.product_price) * cart.product_qentity
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


@register.filter
def printTotal(nu):
    return totalPrice

@register.filter
def emptyTotal(nu):
    global totalPrice
    totalPrice = 0.0
    return ''

@register.filter
def cartCount(carts):
    count = carts.count
    try:
        return int(count)  
    except:
        return len(carts)
    return str(count)



@register.filter
def translation(key,lang0):
    dictionary =  {'Complete the order':'اكمل الطلب'
    ,'Panal':'الاعدادات'
    ,'Products Management':'ادارة المنتجات'
    ,'Orders to be shipped':''
    ,'Edit Product':'تعديل المنتج'
    ,'Shopping Cart':''
    ,'Total':'المجموع'
    ,'Electronic':''
    ,'Book':''
    ,'Search':'بحث'
    ,'Login':'تسجيل الدخول'
    ,'Sign Up':'التسجيل'
    ,'First Name':'الاسم الاول'
    ,'Last Name':'الاسم الأخير'
    ,'User name':'اسم المستخدم'
    ,'Password':'الرقم السري'
    ,'Email':'البريد الاكتروني'
    ,'Mobile Phone':'رقم الجوال'
    ,'Address':'العنوان'
    ,'Address: 816 - 224':'816-224:العنوان'

    ,'Product Name':'اسم المنتج'
    ,'Product Price':'سعر المنتج'
    ,'Product Quntity':'الكمية'
    ,'Product Short Description':'الوصف المختصر للمنتج'
    ,'Product Long Description':'الوصف المطول للمنتج'
    ,'Add Product':'أضف المنتج'
    ,'Add to Cart':'أضف إلى العربة'
    ,'Delete':'حذف'
    ,'Buy':'شراء'

    
    }
    if(lang == 'ar'):
        return dictionary[key]
    return key

@register.filter
def dir(lang0):
    if (lang =='ar'):
        return 'rtl'
    return 'ltr'

@register.filter
def setLang(request):
    global lang
    if(lang=='ar'):
        lang = 'en'
    else:
        lang = 'ar'
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponse("<script>history.go(-1);location.href;</script>")



# < img src = "{% static 'img.png' %}" >
