from django.urls import path, include
from userApp import views

urlpatterns = [
    # http://127.0.0.1:800/user/index
    path('index/', views.index),
    path('login/', views.login),
]