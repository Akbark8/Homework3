from django.contrib import admin
from .models import ClothingItem, Tag

admin.site.register(Tag)
admin.site.register(ClothingItem)
