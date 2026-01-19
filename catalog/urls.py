
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Домашняя с пагинацией
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    # Доп: форма создания
    path('product/create/', views.product_create, name='product_create'),
]