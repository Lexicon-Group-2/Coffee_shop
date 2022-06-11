from django.shortcuts import render
from coffee_store.models import Product
from django.http import HttpResponseRedirect

# Create your views here.

def wish_list(request):
  return render(request, 'wish_list/wish_list.html', {})

def add_to_favorites(request, item_id = None):
  item = Product.objects.filter(id = item_id).first()
  #item.delete()
  return HttpResponseRedirect('/updates')