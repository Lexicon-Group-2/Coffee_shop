from django.urls import path
from . import views

urlpatterns = [
    path('fika_room/', views.fika_room, name='fika_room'),
    path('articles/01', views.article_1, name='article_1'),
    path('articles/02', views.article_2, name='article_2'),
    path('articles/03', views.article_3, name='article_3'),
]
