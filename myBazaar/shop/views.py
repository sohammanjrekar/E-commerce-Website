from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products=Product.objects.all()
    print(products)
    
    params={}
    return render(request ,'shop/index.html',params)

def about(request):
    return render(request ,'shop/about.html')

def blog(request):
    return render(request ,'shop/blog.html') 

def cart(request):
    return render(request ,'shop/cart.html')

def checkout(request):
    return render(request ,'shop/checkout.html')

def contact(request):
    return render(request ,'shop/contact.html')
    
def ordercomplete(request):
    return render(request ,'shop/ordercomplete.html')

def productdetails(request):
    return render(request ,'shop/productdetails.html')

def tracker(request):
    return render(request ,'shop/tracker.html')

def shop(request):
    return render(request ,'shop/shop.html')
   


