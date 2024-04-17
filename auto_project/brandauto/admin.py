from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cars, Category

class CarsAdmin(admin.ModelAdmin):
    # Пропишем метод, который вместо пути для поля photo будет
    # возвращать html-фрагмент (небольшое изображение)
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Photo'

    list_display = ('id', 'brand', 'get_html_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('id', 'brand')
    search_fields = ('brand', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('brand',)}

    fields = ('slug', 'brand', 'color', 'get_html_photo', 'photo', 'description', 'is_published', 'cat',
              'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Cars, CarsAdmin)
admin.site.register(Category, CategoryAdmin)
