from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.models import Profile, User
from .models import Order, OrderItem
from coffee_store.models import Product
from django.http import JsonResponse
import json
# Create your views here.

def cart(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    items = order.orderitem_set.all()
  else:
    items = []
    order = ""
  context = {'products': items, 'order': order}
  return render(request, 'shopping_cart/cart.html', context)


def checkout(request):
  return render(request, 'shopping_cart/checkout.html', {})


def update_item(request):
  data = json.loads(request.body)
  productId = data['productId']
  action = data['action']
  print('Action:', action)
  print('Product:', productId)

  customer = request.user.customer
  product = Product.objects.get(id=productId)
  order, created = Order.objects.get_or_create(customer=customer, completed=False)
  
  orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

  if action == 'add' or action == 'increase':
    orderItem.quantity = (orderItem.quantity + 1)
  
  elif action == 'decrease':
    orderItem.quantity = (orderItem.quantity - 1)
  
  orderItem.save()

  if action == 'remove':
    orderItem.delete()
  
  if orderItem.quantity < 1:
    orderItem.delete()
  
  return JsonResponse('Item updated', safe=False)


def confirm_order(request):
  customer = request.user.customer
  order = Order.objects.get(customer=customer, completed=False)
  order.completed = True
  order.save()
  return render(request, 'main/homepage.html')


def user(request):
  customer = request.user.customer
  orders = Order.objects.filter(customer=customer, completed=True).order_by("-date_ordered")
  
  context = {
    'orders': orders,
  }

  return render(request, 'shopping_cart/user.html', context)

def order_detail(request, order_id=None):
  items = OrderItem.objects.filter(order=order_id)
  order = Order.objects.get(id=order_id)
  print(order.get_cart_total)
  for i in items.iterator():
    print(i.id)

  
  customer = request.user.customer
  order2 = Order.objects.get(customer=customer, completed=False).orderitem_set.all()
  in_cart = [i.product.id for i in order2.iterator()]
  
  context = {
    'products': items,
    'order': order,
    'cart': in_cart,
  }
  return render(request, 'shopping_cart/order_detail.html', context)