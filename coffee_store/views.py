from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.models import Profile, User
from .models import Product

def sort_items(request, products):
  sort_by = request.GET.get("sort", "low-to-high") 
  if sort_by == "low-to-high": products = products.order_by("price")
  if sort_by == "high-to-low": products = products.order_by("-price")
  if sort_by == "alpha":       products = products.order_by("title")
  return products


def store(request):
  context = {}
  return render(request, 'coffee_store/store.html', context)

def coffee_machines(request):
  products = Product.objects.filter( category__name__contains="Coffee machines" )
  products = sort_items(request, products)
  context = {'products' : products}
  return render(request, 'coffee_store/coffee_machines.html', context)

def coffee_types(request):
  products = Product.objects.filter( category__name__contains="Coffee Beans" )
  products = sort_items(request, products)
  context = {'products' : products}
  return render(request, 'coffee_store/coffee_types.html', context)

def coffee_mugs(request):
  return render(request, 'coffee_store/coffee_mugs.html', {})

def other_accessories(request):
  return render(request, 'coffee_store/other_accessories.html', {})

def cart(request):
  context = {}
  return render(request, 'coffee_store/cart.html', context)

def checkout(request):
  return render(request, 'coffee_store/checkout.html', {})