from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from shop_cart import *
from shop_app.models import *
from shop_cart.models import *
from .models import *

# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['name']      # maps to User.username
        email_id = request.POST['email']        # maps to User.email
        phone_number = request.POST['phn_num']
        password = request.POST['pass']
        confirm_password = request.POST['conpass']

        if password == confirm_password:

        #
        # # ✅ Check if username already exists
            if Cutomer_register.objects.filter(username=username).exists():
                messages.warning(request, "Username already exists")
                return redirect('register')
            elif Cutomer_register.objects.filter(email_id=email_id).exists():
                messages.warning(request, "Email already exists")
                return redirect('register')

            # ✅ Create user (this goes into auth_user table)
            else:
                user=Cutomer_register.objects.create(
                    username=username,
                    email_id=email_id,
                    phone_number=phone_number,
                    password=password
                )
                user.save();
                print("user created")
                messages.success(request, "Registration successful! Please login.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # ✅ Create profile and link with user
        # profile.objects.create(
        #     user=user,
        #     phone_number=phone_number,
        #     car_number=car_number
        # )

        # messages.success(request, "User registered successfully")
        # return redirect('/')  # redirect after success
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('pass')

        try:
            user = Cutomer_register.objects.get(username=username)

            if user.password == password:
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                messages.success(request, "Login successful")
                return redirect('/',{"username":username})  # change to your home page
            else:
                messages.error(request, "Invalid password")
                return redirect('login')

        except Cutomer_register.DoesNotExist:
            messages.error(request, "User does not exist")
            return redirect('login')

    return render(request, "login.html")

def logout(request):
    request.session.flush()   # clears all session data
    messages.success(request, "You have been logged out successfully")
    return redirect('/')