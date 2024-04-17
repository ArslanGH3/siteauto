from django.db.models import Count, Q

from .models import Category, Menu



# Функция для получения списка категорий автомобилей
def get_cats_auto():
    cats = Category.objects.annotate(Count('cars')).order_by('id')
    return cats



# Миксин для классов представлений
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        context['cats'] = get_cats_auto()
        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        if not self.request.user.is_authenticated:
            menu = Menu.objects.filter(~Q(url_name='add_page'))
        else:
            menu = Menu.objects.all()

        context['menu'] = menu
        return context
