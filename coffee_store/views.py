from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.models import Profile, User

# Create your views here.

def store(request):
  return render(request, 'coffee_store/store.html', {})


def coffee_machines(request):
  return render(request, 'coffee_store/coffee_machines.html', {})


def coffee_types(request):
  return render(request, 'coffee_store/coffee_types.html', {})


def coffee_mugs(request):
  return render(request, 'coffee_store/coffee_mugs.html', {})


def other_accessories(request):
  return render(request, 'coffee_store/other_accessories.html', {})


def cart(request):
  return render(request, 'coffee_store/cart.html', {})
