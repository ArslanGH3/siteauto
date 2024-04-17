from rest_framework import generics
from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from brandauto.utils import DataMixin
from .forms import RegisterUserForm, LoginUserForm
from .serializers import GetUPDataSerializer


# Регистрация
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        context.update(c_def)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



# Авторизация
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        context.update(c_def)
        return context

    def get_success_url(self):
        return reverse_lazy('home')




# Выход из учетной записи
def logout_user(request):
    logout(request)
    return redirect('login')



# Представление DRF для получения данных о пользователе.
# Только для авторизованных пользователей
class GetUPDataAPI(generics.ListAPIView):
    serializer_class = GetUPDataSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return get_user_model().objects.filter(pk=self.request.user.pk)

