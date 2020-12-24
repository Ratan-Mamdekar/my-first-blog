from django.urls import path
from . import views

urlpatterns = [
    path('home', views.post_list, name='post_list'),
    path('page2', views.post_list, name='post_list'),
    path('welcome', views.welcome, name='welcome'),
]
