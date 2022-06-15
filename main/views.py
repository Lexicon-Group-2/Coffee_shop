from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.forms  import UserForm, UserProfileForm
from main.models import Profile

# an email should be unique, we will use this little fix
# User._meta.get_field('email')._unique = True


from django import template

register = template.Library()
@register.simple_tag
def number_of_messages(request):
    num_items = 80
    return num_items


def signup(request):
  registered = False

  if request.method == 'POST':
    user_form = UserForm(data = request.POST)
    profile_form = UserProfileForm(data = request.POST)

    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      #auth_login(request, user) # this will automatically log in user after creating an account
      user.set_password(user.password)
      user.save()
      
      profile = profile_form.save(commit=False)
      profile.user = user

      if 'image' in request.FILES:
        profile.image = request.FILES['image']
        profile.save()
        
      registered = True
    else:
      print(user_form.errors, profile_form.errors)
  else:
    user_form = UserForm()
    profile_form = UserProfileForm()

  context = {
    'user_form': user_form,
    'profile_form': profile_form,
    'registered': registered,
  }

  return render(request, 'main/signup.html', context)

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    # use django authentication function
    user = authenticate(username=username, password=password)
    
    # check if user passed the authentication process
    if user:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
      else:
        return HttpResponse("Account not active")
    else:
      return HttpResponse("Invalid login details!")

  return render(request, 'main/login.html', {})

@login_required
def user_logout(request):
  logout(request)
  return render(request, 'main/logout.html', {})

# This view was moved to the shopping_cart app
#def user(request):
#  return render(request, 'main/user.html', {})

# welcome page
def index(request):
  return render(request, 'main/index.html', {})

def home(request): 
  return render(request, 'main/homepage.html',{})


