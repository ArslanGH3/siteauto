from django.db import models
from django.urls import reverse

# Модель с категориями машин
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


# Модель с марками машин
class Cars(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    brand = models.CharField(max_length=255, verbose_name='Марка')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['id']


# Модель с пунктами меню
class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок меню')
    url_name = models.CharField(max_length=255, verbose_name='URL меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['id']