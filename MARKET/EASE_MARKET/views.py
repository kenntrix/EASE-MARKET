from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactUs, Seller, Goods_detail, Client
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
    
def home_view(request):
    if request.user.is_authenticated:
        goods = Goods_detail.objects.all()
        categories = Goods_detail.CATEGORY_CHOICES
        clients = Client.objects.all()
        sellers = Seller.objects.all()

        context = {
            'goods': goods,
            'categories': categories,
            'clients': clients,
            'sellers': sellers
        }
        return render(request, 'EASE_MARKET/home.html', context)
    else:
        messages.error(request,"Login to continue ...")
        return redirect('login')
    
    
def index(request):
    search_query = request.GET.get('search_query', '')
    goods = Goods_detail.objects.filter(name__icontains=search_query)
    context = {'goods': goods}
    return render(request, 'EASE_MARKET/home.html', context)



def login_view(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request,f"Login as { email }, Successfully!")
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
                return redirect('login')
            
        
        return render(request, 'EASE_MARKET/login.html');


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        
        if password != password_confirmation:
            messages.error(request,"Passwords do not match")
            return redirect('signin')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"email already exists, go to login to proceed ")
            return redirect('signin')
            

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists")
            return redirect('signin')
        
        if username:
            user  = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            user.save()
            messages.success(request,"Account successfully created")
            return redirect('login')
        else:
            messages.error(request,"Please enter a username")
            return render(request,'EASE_MARKET/signup.html')
        
    return render(request,'EASE_MARKET/signup.html')

def about_view(request):
    return render(request, 'EASE_MARKET/about.html');

def service_view(request):
    if request.user.is_authenticated:
        
        return render(request, 'EASE_MARKET/service.html');
    else:
        messages.error(request,"Login to continue ...")
        return redirect('login')

from django.shortcuts import render, get_object_or_404
from .models import Goods_detail, Seller


def item_detail(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Goods_detail, pk=pk)
        goods = Goods_detail.objects.all()
        categories = Goods_detail.CATEGORY_CHOICES
        sellers = Seller.objects.all()
        context = {
            'goods': goods,
            'categories': categories,
            'item': item,
            'sellers': sellers
        }
        return render(request, 'EASE_MARKET/item.html', context)
    
    else:
        messages.error(request, "Please login to continue.")
        return redirect('item')


    
def contact_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            contact = ContactUs(
                username=username,
                email=email,
                subject=subject,
                message=message,
            )
            contact.save()
            messages.success(request, "The message was delivered successfully")
            return redirect('contact')
        
        return render(request, 'EASE_MARKET/contact.html');
    else:
        messages.error(request,"Login to continue ...")
        return redirect('login')
    
    
def seller_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            id_number = request.POST.get('id_number')
            current_location = request.POST.get('current_location')
            price = request.POST.get('price')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone_no = request.POST.get('phone_no')
            item_image = request.POST.get('img')
            
            seller = Seller(
                username=username,
                id_number=id_number,
                current_location = current_location,
                price=price,
                email=email,
                address=address,
                phone_no=phone_no, 
                item_image=item_image,
            )
            seller.save()
            messages.success(request, "Your product has been uploaded successfully, Market another product !")
            return redirect('seller')
        
        return render(request, 'EASE_MARKET/seller.html');
    else:
        messages.error(request,"Login to continue ...")
        return redirect('login')
            

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect('login')