from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Your password and confirm password are not the same!")
            return redirect('signup')
        elif User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Username or password is incorrect!")
            return redirect('login')

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')


def index(request):
    return render(request,'index.html')

def order(request):
    return HttpResponse("hello")


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER', 'index')  # Fallback to 'index' if no next URL is provided
    return redirect(next_url)

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'cart_items': cart_items})



def products_by_category(request, category_name):
    products = Product.objects.filter(category=category_name)
    return render(request, 'products.html', {'products': products, 'category_name': category_name})