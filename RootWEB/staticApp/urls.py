
from django.urls import path, include
from staticApp import views

urlpatterns =[
    path('index/', views.index, name='static_index'),
    path('line/', views.line, name='static_line'),
    path('bar/', views.bar, name='static_bar'),

]