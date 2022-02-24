
from django.urls import path, include
from bbsApp import views

urlpatterns =[
    path('index/', views.index, name='bbs')
]