from django.urls import path
from . import views

urlpatterns = [
    path('wish_list/', views.wish_list, name="wish_list"),
]
