from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='lbm.add'),
    path('edit/<int:id>', views.edit, name='lbm.edit'),
    path('delete/<int:id>', views.delete, name='lbm.delete'),
]
