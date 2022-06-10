from django.shortcuts import render
#from coffee_store.models import Product

# Create your views here.

def wish_list(request):
  return render(request, 'wish_list/wish_list.html', {})