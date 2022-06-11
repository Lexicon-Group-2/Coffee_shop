from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.forms import NullBooleanField
from django.utils import timezone


class Category(models.Model):
  name = models.CharField(max_length=50, unique=True)
  
  def __str__(self):
    return self.name
  
  class Meta:  
    verbose_name_plural = 'Categories' 

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  short_desc = models.TextField(max_length=100, blank=True)
  long_desc = models.TextField(max_length=500, blank=True)
  image1 = models.ImageField(upload_to='product_images', blank=True)
  image2 = models.ImageField(upload_to='product_images', blank=True)
  price = models.IntegerField()
  url   = models.URLField(blank=True)
  favourites = models.ManyToManyField(User, related_name='favourites', default=None, blank=True)
  
  def __str__(self):
    return self.title
