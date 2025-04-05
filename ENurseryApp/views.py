from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .model_loader import model, preprocess_image
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, Product, Category
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def Welcome(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')
    

def contact(request):
    return render(request,'contact.html')
    

def products(request):
    products = None
    category = Category.get_all_category();

    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_category_id_get_all_product(categoryID)
    else:
        products = Product.get_all_products() 
    data = {}
    data["products"] = products
    data["category"] = category
    return render(request, 'products.html',data)

    

# ========================== Registration Function =====================
def registration(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pas = request.POST.get('password')
        address = request.POST.get('add')
        pin = request.POST.get('pincode')

        my_user = CustomUser.objects.create_user(username=uname, email=email, password=pas)
        my_user.address = address
        my_user.pin = pin
        my_user.save()
        return redirect('login')
    return render(request, "registration.html")

#===================== Login Function ========================

def login_view(request):
    if request.method == "POST":
        email= request.POST.get('email')
        pas = request.POST.get('password')
        print(email,pas)
        user = authenticate(request,CustomUser=email,password=pas)
        print(user)

        try:
            user_obj = User.objects.get(email=email)  # Find user by email
            user = authenticate(request, username=user_obj.username, password=pas)  # Authenticate using username
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request,user) 
            return redirect('user')
        else:
            return HttpResponse("User name or password is incorrect")
    return render(request, "login.html")


# ====================== User page after Login ===================

@login_required(login_url='login')
def user(request):
    return render(request,"user.html")

# ============== LogOut Function ==================

def logout_view(request):  # Changed function name
    logout(request)  # Calls Django's built-in logout function
    return redirect('home')