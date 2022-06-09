from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('store/coffee_machines', views.coffee_machines, name='coffee_machines'),
    path('store/coffee_types', views.coffee_types, name='coffee_types'),
    path('store/coffee_mugs', views.coffee_mugs, name='coffee_mugs'),
    path('store/other_accessories', views.other_accessories, name='other_accessories'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    
]


