from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from shop_cart import *
from shop_app.models import *
from shop_cart.models import *

# Create your views here.
# Cart id
def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def checkout(request,total=0,count=0,cart_items=None):
    ct_items = []
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct)
        for i in ct_items:
            total += (i.products.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'checkout.html',{"ci":ct_items,"t":total,"cn":count})