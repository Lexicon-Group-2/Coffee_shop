from django import forms
from django.contrib.auth.models import User
from main.models import Profile


class UserForm(forms.Form, forms.ModelForm):
  # The class 'form-control' is a bootstrap class
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  email    = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  
  class Meta():
    model = User
    fields = ['username', 'email', 'password']
    
class UserProfileForm(forms.ModelForm):
  image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control custom-file-input'}))
  class Meta():
    model = Profile
    fields = ['image']

