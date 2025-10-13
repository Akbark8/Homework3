from django.shortcuts import render, redirect
from .models import BasketItem, Customer
from books.models import Book

def basket_list(request):
    items = BasketItem.objects.all()
    return render(request, 'basket/basket_list.html', {'basket_items': items})

def add_to_basket(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        book_id = request.POST.get('book')
        quantity = int(request.POST.get('quantity', 1))

        customer = Customer.objects.get(id=customer_id)
        book = Book.objects.get(id=book_id)

        BasketItem.objects.create(customer=customer, book=book, quantity=quantity)
        return redirect('basket_list')

    customers = Customer.objects.all()
    books = Book.objects.all()
    return render(request, 'basket/add_to_basket.html', {'customers': customers, 'books': books})
