from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, 'app/home.html', context)
def cart(request):
    context={}
    return render(request, 'app/cart.html', context)
def checkout(request):
    context={}
    return render(request, 'app/checkout.html', context)

    
