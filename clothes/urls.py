from django.urls import path
from . import views

urlpatterns = [
    path('men/', views.MenClothesListView.as_view(), name='men_clothes'),
    path('women/', views.WomenClothesListView.as_view(), name='women_clothes'),
    path('kids/', views.KidsClothesListView.as_view(), name='kids_clothes'),
    path('search/', views.SearchClothesListView.as_view(), name='search_clothes'),
]
