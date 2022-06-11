from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.models import Profile, User
from .models import Product

# this function will sort the items based on user input
def sort_items(request, products):
  sort_by = request.GET.get("sort", "low-to-high") 
  if sort_by == "low-to-high": products = products.order_by("price")
  if sort_by == "high-to-low": products = products.order_by("-price")
  if sort_by == "alpha":       products = products.order_by("title")
  return products

# it will return the product dictionary with certain category
def prod_dict(request, category):
  products = Product.objects.filter( category__name__contains=category )
  products = sort_items(request, products)
  return {'products' : products}


def store(request):
  context = {}
  return render(request, 'coffee_store/store.html', context)

def coffee_machines(request):
  context = prod_dict(request, "Coffee machines")
  return render(request, 'coffee_store/coffee_machines.html', context)

def coffee_types(request):
  context = prod_dict(request, "Coffee Beans")
  return render(request, 'coffee_store/coffee_types.html', context)

def coffee_mugs(request):
  context = prod_dict(request, "Coffee mugs")
  return render(request, 'coffee_store/coffee_mugs.html', context)

def other_accessories(request):
  return render(request, 'coffee_store/other_accessories.html', {})

def cart(request):
  context = {}
  return render(request, 'coffee_store/cart.html', context)

def checkout(request):
  return render(request, 'coffee_store/checkout.html', {})