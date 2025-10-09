from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Книги
class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название книги")
    description = models.TextField(verbose_name="Описание книги")
    image = models.ImageField(upload_to='books/', verbose_name="Обложка")
    quantity_page = models.PositiveIntegerField(verbose_name="Количество страниц")
    author = models.CharField(max_length=255, verbose_name="Автор")
    book_audio = models.URLField(verbose_name="Ссылка на аудиокнигу")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

# Отзывы
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', verbose_name='Книга')
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Оценка (1–5)'
    )
    text = models.TextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.book.title} — {self.rating}★"

# Тур
class Tour(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название тура')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

# Человек
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')

    def __str__(self):
        return self.name

# Регистрация на тур (один человек на один тур)
class Registration(models.Model):
    person = models.OneToOneField('Person', on_delete=models.CASCADE, verbose_name='Человек')
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, verbose_name='Тур')

    def __str__(self):
        return f"{self.person.name} — {self.tour.name}"
