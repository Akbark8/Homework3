from django.shortcuts import render
from .models import ClothingItem

def men_clothes(request):
    items = ClothingItem.objects.filter(category='men')
    return render(request, 'clothes/men_list.html', {'items': items})

def women_clothes(request):
    items = ClothingItem.objects.filter(category='women')
    return render(request, 'clothes/women_list.html', {'items': items})

def kids_clothes(request):
    items = ClothingItem.objects.filter(category='kids')
    return render(request, 'clothes/kids_list.html', {'items': items})

def search_clothes(request):
    query = request.GET.get('q', '')
    items = ClothingItem.objects.filter(name__icontains=query)
    return render(request, 'clothes/search.html', {'items': items, 'query': query})
