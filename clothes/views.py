from django.views.generic import ListView
from .models import ClothingItem

class MenClothesListView(ListView):
    model = ClothingItem
    template_name = 'clothes/men_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return ClothingItem.objects.filter(category='men')


class WomenClothesListView(ListView):
    model = ClothingItem
    template_name = 'clothes/women_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return ClothingItem.objects.filter(category='women')


class KidsClothesListView(ListView):
    model = ClothingItem
    template_name = 'clothes/kids_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return ClothingItem.objects.filter(category='kids')


class SearchClothesListView(ListView):
    model = ClothingItem
    template_name = 'clothes/search.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return ClothingItem.objects.filter(name__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
