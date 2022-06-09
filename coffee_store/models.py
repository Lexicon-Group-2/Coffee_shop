from tkinter import CASCADE
from tokenize import blank_re
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.forms import NullBooleanField
from django.utils import timezone


class CoffeeMachine(models.Model):
  title = models.CharField(max_length=100)
  short_desc = models.TextField(max_length=100, blank=True)
  long_desc = models.TextField(max_length=500, blank=True)
  image1 = models.ImageField(upload_to='coffee_machines')
  image2 = models.ImageField(upload_to='coffee_machines', blank=True)
  price = models.IntegerField()
  url   = models.URLField()

  def __str__(self):
    return self.title

  class Meta:  
    verbose_name_plural = 'Coffee Machines'


class CoffeeMugs(models.Model):
  title = models.CharField(max_length=100)
  short_desc = models.TextField(max_length=100, blank=True)
  long_desc = models.TextField(max_length=500, blank=True)
  image1 = models.ImageField(upload_to='coffee_mugs')
  image2 = models.ImageField(upload_to='coffee_mugs', blank=True)
  price = models.IntegerField()
  url   = models.URLField()

  def __str__(self):
    return self.title

  class Meta:  
    verbose_name_plural = 'Coffee Mugs'



class CoffeeBeans(models.Model):
  title = models.CharField(max_length=100)
  short_desc = models.TextField(max_length=100, blank=True)
  long_desc = models.TextField(max_length=500, blank=True)
  image1 = models.ImageField(upload_to='coffee_beans')
  image2 = models.ImageField(upload_to='coffee_beans', blank=True)
  price = models.IntegerField()
  url   = models.URLField()

  def __str__(self):
    return self.title

  class Meta:  
    verbose_name_plural = 'Coffee Beans'


class Accessory(models.Model):
  title = models.CharField(max_length=100)
  short_desc = models.TextField(max_length=100, blank=True)
  long_desc = models.TextField(max_length=500, blank=True)
  image1 = models.ImageField(upload_to='accessories')
  image2 = models.ImageField(upload_to='accessories', blank=True)
  price = models.IntegerField()
  url   = models.URLField()

  def __str__(self):
    return self.title
  
  class Meta:  
    verbose_name_plural = 'Accessories'
