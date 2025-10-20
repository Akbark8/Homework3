from django.urls import path
from . import views

urlpatterns = [
    path('', views.BasketListView.as_view(), name='basket_list'),
    path('add/', views.BasketItemCreateView.as_view(), name='add_to_basket'),
    path('update/<int:pk>/', views.BasketItemUpdateView.as_view(), name='update_basket_item'),
    path('delete/<int:pk>/', views.BasketItemDeleteView.as_view(), name='delete_basket_item'),
]
