from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, DetailView

from .default_my_settings import DEFAULT_CAR_IMAGE
from .models import Cars, Menu, Category
from .utils import DataMixin, get_cats_auto
from .forms import AddPostForm, ContactForm

# Класс основной страницы с постами
class HomePage(DataMixin, ListView):
    model = Cars
    template_name = 'brandauto/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        common_info = self.get_user_context(title='Главная страница')
        context['DEFAULT_CAR_IMAGE'] = DEFAULT_CAR_IMAGE
        context.update(common_info)
        return context

    def get_queryset(self):
        return Cars.objects.filter(is_published=True).select_related('cat')



# Представление по категориям автомобилей (левый сайдбар)
class CarsCategory(DataMixin, ListView):
    model = Cars
    template_name = 'brandauto/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Cars.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=f'Категория - {str(c.name)}', cat_selected=c.pk)
        context['DEFAULT_CAR_IMAGE'] = DEFAULT_CAR_IMAGE
        context.update(c_def)
        return context



# Функция представление "О сайте"
def about(request):
    if not request.user.is_authenticated:
        menu = Menu.objects.filter(~Q(url_name='add_page'))
    else:
        menu = Menu.objects.all()
    cats = get_cats_auto()
    return render(request, 'brandauto/about.html', {'menu': menu,
                                                    'title': 'О сайте',
                                                    'cats': cats})



# Добавление статьи
class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'brandauto/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        context.update(c_def)
        return context



# Обратная связь
class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'brandauto/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        context.update(c_def)
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')



# Страница с постом
class ShowPost(DataMixin, DetailView):
    model = Cars
    template_name = 'brandauto/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'].brand)
        context['DEFAULT_CAR_IMAGE'] = DEFAULT_CAR_IMAGE
        context.update(c_def)
        return context



