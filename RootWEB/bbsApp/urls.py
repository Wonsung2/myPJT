
from django.urls import path, include
from bbsApp import views

urlpatterns =[
    path('index/', views.index, name='bbs_index'),
    path('createForm/', views.createForm, name='bbs_createForm'),
    path('bbs_create/', views.create, name='bbs_create'),
    path('bbs_read/', views.read, name='bbs_read'),
    path('bbs_remove/', views.remove, name='bbs_remove'),
    path('bbs_update/', views.update, name='bbs_update'),
    path('bbs_search/', views.search, name='bbs_search'),
]