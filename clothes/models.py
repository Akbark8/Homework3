from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ClothingItem(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'Мужская одежда'),
        ('women', 'Женская одежда'),
        ('kids', 'Детская одежда'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    tags = models.ManyToManyField(Tag, related_name='clothes')

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
