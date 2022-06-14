from ctypes import addressof
from types import CoroutineType
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from coffee_store.models import Product


class Customer(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
	
  def __str__(self):
    return " ".join([self.first_name, self.last_name])


class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True,  blank=True)
  date_ordered = models.DateTimeField(auto_now_add=True)
  completed = models.BooleanField(default=False)
  transaction_id = models.CharField(max_length=100, null=True)

  def __str__(self):
    return str(self.id)
  
  @property
  def get_cart_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([i.get_total for i in orderitems])
    return total
  
  @property
  def get_cart_items(self):
    orderitems = self.orderitem_set.all()
    total = sum([i.quantity for i in orderitems])
    return total


class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
  order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
  quantity = models.IntegerField(default=0, null=True, blank=True)
  date_added = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.product.title)

  @property
  def get_total(self):
    total = self.product.price * self.quantity
    return total

class ShippingAddress(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
  order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
  address = models.CharField(max_length=200, null=False)
  city = models.CharField(max_length=200, null=False)
  state = models.CharField(max_length=200, null=False)
  zipcode = models.CharField(max_length=200, null=False)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.address
  
  class Meta:
    verbose_name_plural = 'Shipping Address'







