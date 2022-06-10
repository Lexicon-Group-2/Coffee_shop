from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name="logout"),
    path('user/', views.user, name="user"),
    path('home/',views.home,name='home')

]
