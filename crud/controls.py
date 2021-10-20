from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('base/', views.Base, name='base'),
    path('add/', views.Add, name='add'),
    path('delete/<int:pk>/', views.Delete, name='delete'),
    path('edit/<int:pk>/', views.Edit, name='edit'),

]
