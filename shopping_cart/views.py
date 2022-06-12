from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.models import Profile, User
from .models import Order
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