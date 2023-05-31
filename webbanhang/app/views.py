from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'app/home.html', context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, creates = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []  
        order = {'get_cart_items':0, 'get_cart_total':0}  
    context={'items':items, 'order':order}
    return render(request, 'app/cart.html', context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, creates = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []  
        order = {'get_cart_items':0, 'get_cart_total':0}  
    context={'items':items, 'order':order}
    return render(request, 'app/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    producId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id = producId)
    order, creates = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, creates = OrderItem.objects.get_or_create(order = order,product  = product, complete = False)
    if action == 'add' :
        orderItem.quantity += 1
    elif action == 'remove' :
        orderItem.quantity -= 1
    orderItem.save()
    if OrderItem.quantity<=0:
        orderItem.delete()        
    return JsonResponse('added',safe=False)
    
