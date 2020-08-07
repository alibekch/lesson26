from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from products.models import *
from orders.models import *

def make_order(request, id_product):
    userObject = request.user
    product = Product.objects.get(pk=id_product)
    order = Order(user= user, product=product)
    order.save()
    return redirect("main_page")


def log_out(request):
    logout(request)
    return redirect ("login_page")


def main_page(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "main/home.html", context)

def login_page(request):
    error = ""
    if request.method == "POST":
        username = request.POST['form_username']
        password = request.POST['form_pass']
        
        if len(username)==0 or len(password) == 0:
            error="заполните верно поля пользователя и пароль"
        else:
            userObject = authenticate(request, username = username, password = password)
            if userObject is None:
                error = "NO SUCH USER"
            else:
                login(request, userObject)
                return redirect("main_page")

    context = {"error": error}

        
    return render(request, "main/login.html", context)


def register_page(request):
    error = ""
    
    if request.method == "POST":
        firstName = request.POST['form_name']
        lastName = request.POST['form_surname']
        email = request.POST['form_email']
        username = request.POST['form_username']
        password = request.POST['form_pass']
        dateRegistration = request.POST['form_year']

        if firstName =="" or lastName=="" or email=="" or username=="" or password =="":
            error = " INVALID INPUT, TRY AGAIN FILLING ALL FIELDS"
        
        else:

            user = User.objects.create_user(
                first_name = firstName,
                last_name = lastName,
                email = email,
                username = username,
                password = password
            )
            user.save()

            error = firstName+" "+ lastName+" "+ dateRegistration
        
    
    context = {"error": error}
    return render(request, "main/register.html", context)
# Create your views here.

