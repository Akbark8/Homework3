from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket_list, name='basket_list'),
    path('add/', views.add_to_basket, name='add_to_basket'),
]
