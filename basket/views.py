from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BasketItem, Customer
from books.models import Book


class BasketListView(ListView):
    model = BasketItem
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket_items'


class BasketItemUpdateView(UpdateView):
    model = BasketItem
    fields = ['quantity']
    template_name = 'basket/update_basket_item.html'
    success_url = reverse_lazy('basket_list')


class BasketItemDeleteView(DeleteView):
    model = BasketItem
    template_name = 'basket/delete_basket_item.html'
    success_url = reverse_lazy('basket_list')


class BasketItemCreateView(View):
    def get(self, request):
        customers = Customer.objects.all()
        books = Book.objects.all()
        return render(request, 'basket/add_to_basket.html', {'customers': customers, 'books': books})

    def post(self, request):
        customer_id = request.POST.get('customer')
        book_id = request.POST.get('book')
        quantity = int(request.POST.get('quantity', 1))
        customer = Customer.objects.get(id=customer_id)
        book = Book.objects.get(id=book_id)
        BasketItem.objects.create(customer=customer, book=book, quantity=quantity)
        return redirect('basket_list')
