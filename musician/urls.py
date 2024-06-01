from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='mus.add'),
    path('edit/<int:id>', views.edit, name='mus.edit'),
    path('delete/<int:id>', views.delete, name='mus.delete'),
]