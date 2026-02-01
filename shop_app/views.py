from itertools import product
from zoneinfo import available_timezones
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import shop, categories
from .forms import UpdateForm
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
# def demo(request):
#     return HttpResponse("hello world")

def index(request,c_slug=None):
    c_page=None
    prod=None
    if c_slug!=None:
        c_page=get_object_or_404(categories,slug=c_slug)
        prod=shop.objects.filter(category=c_page,available=True)
    else:
        prod=shop.objects.all().filter(available=True)
    category=categories.objects.all()
    # product=shop.objects.all()
    paginator=Paginator(prod,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=Paginator.page(paginator.num_pages)
    return render(request,"index.html",{'products':prod,'category':category,'page':pro})
# def cart(request):
#     return render(request,"cart.html")
def home(request):
    return render(request,"cart.html")
def details(request,shop_id):
    product1=shop.objects.get(id=shop_id)
    return render(request,"details.html",{'product':product1})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        img=request.FILES['img']
        cat_id=request.POST.get('category')

        cat_obj = categories.objects.get(id=cat_id)

        s=shop(name=name,desc=desc,img=img,price=price,category=cat_obj)
        s.save()
        print(":) Product Added Successfully (:")
        return redirect('/')
    cats = categories.objects.all()
    return render(request, "add.html", {"categories": cats})
def update(request,id):
    obj=shop.objects.get(id=id)
    form=UpdateForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,"update.html",{'form':form,'obj':obj})
def delete(request,id):
    if request.method=='POST':
        obj=shop.objects.get(id=id)
        obj.delete()
        print(":( Product Deleted Successfully ):")
        return redirect('/')
    return render(request,"delete.html")
def category(request,cat):
    filtered=shop.objects.filter(category=cat)
    return render(request,"index.html",{'filtered':filtered,'category':cat})

def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")
def search(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=shop.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))

    return render(request,"search.html",{'qr':query,'pr':prod})


