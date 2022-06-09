from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.models import Profile, User
from .models import CoffeeMachine


# Create your views here.

def store(request):
  context = {}
  return render(request, 'coffee_store/store.html', context)


def coffee_machines(request):
  products = CoffeeMachine.objects.all()
  context = {'products' : products}
  return render(request, 'coffee_store/coffee_machines.html', context)


def coffee_types(request):
  return render(request, 'coffee_store/coffee_types.html', {})


def coffee_mugs(request):
  return render(request, 'coffee_store/coffee_mugs.html', {})


def other_accessories(request):
  return render(request, 'coffee_store/other_accessories.html', {})


def cart(request):
  context = {}
  return render(request, 'coffee_store/cart.html', context)

def checkout(request):
  return render(request, 'coffee_store/checkout.html', {})