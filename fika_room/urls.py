from django.urls import path
from . import views

urlpatterns = [
    path('fika_room/', views.fika_room, name='fika_room'),
]
