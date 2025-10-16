from django.urls import path
from . import views

urlpatterns = [
    path('men/', views.men_clothes, name='men_clothes'),
    path('women/', views.women_clothes, name='women_clothes'),
    path('kids/', views.kids_clothes, name='kids_clothes'),
    path('search/', views.search_clothes, name='search_clothes'),
]
