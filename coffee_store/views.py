from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.models import Profile, User
from .models import Product
from shopping_cart.models import Order

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
  
  if request.user.is_authenticated:
    liked = [i.id for i in products.filter(favourites=request.user).iterator()]
    customer = request.user.customer
    order = Order.objects.get(customer=customer, completed=False).orderitem_set.all()
    items = [i.product.id for i in order.iterator()]
  else:
    liked = []
    items = []
    order = ""
  context = {
        'products' : products,
        'category' : category,
        'favourites' : liked,
        'cart' : items,
    }
  print(items)
  return context


def store(request):
  return render(request, 'coffee_store/store.html', {})

def coffee_machines(request):
  context = prod_dict(request, "Coffee machines")
  return render(request, 'coffee_store/coffee_machines.html', context)

def coffee_types(request):
  context = prod_dict(request, "Coffee beans")
  return render(request, 'coffee_store/coffee_types.html', context)

def coffee_mugs(request):
  context = prod_dict(request, "Coffee mugs")
  return render(request, 'coffee_store/coffee_mugs.html', context)

def other_accessories(request):
  context = prod_dict(request, "Coffee Accessories")
  return render(request, 'coffee_store/other_accessories.html', context)

def wish_list(request):
  if request.user.is_authenticated:
    products = Product.objects.filter(favourites=request.user)
    liked = [i.id for i in products.filter(favourites=request.user).iterator()]
    customer = request.user.customer
    order = Order.objects.get(customer=customer, completed=False).orderitem_set.all()
    items = [i.product.id for i in order.iterator()]
  else:
    products, liked, items = [], [], []
    order = ""
  
  context = {
        'products' : products,
        'cart' : items,
    }
  return render(request, 'coffee_store/wish_list.html', context)

@login_required
def add_to_favourite(request, id):
  item = get_object_or_404(Product, id=id)
  if item.favourites.filter(id=request.user.id).exists():
    item.favourites.remove(request.user)
  else:
    item.favourites.add(request.user)
  return HttpResponseRedirect(request.META['HTTP_REFERER'])
