from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.update_item, name='update_item'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('user/', views.user, name="user"),
    path('order/<order_id>', views.order_detail, name="order_detail"),
]


