from itertools import product

from django.shortcuts import render,redirect,get_object_or_404
from django.utils.translation.trans_null import activate

from shop_app.models import *
from shop_cart.models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart(request,total=0,count=0,cart_items=None):
    ct_items = []
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct)
        for i in ct_items:
            total +=(i.products.price*i.quantity)
            count +=i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,"cart.html", {"ci":ct_items,"t":total,"cn":count})
def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id
def add_item(request, product_id):
    product=shop.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()

    try:
        c_items=items.objects.get(products=product,cart=ct)
        if c_items.quantity < c_items.products.stock:
            c_items.quantity+=1
        c_items.save()

    except items.DoesNotExist:
        c_items=items.objects.create(products=product,quantity=1,cart=ct)
        c_items.save()
    return redirect("cart")

def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(shop,id=product_id)
    c_items=items.objects.get(products=prod,cart=ct)
    if c_items.quantity >1:
        c_items.quantity -=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart')

def delete_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(shop, id=product_id)
    c_items=items.objects.get(products=prod,cart=ct)
    # if c_items==0:
    #     print("cart is empty")
    # else:
    c_items.delete()

    return redirect('cart')