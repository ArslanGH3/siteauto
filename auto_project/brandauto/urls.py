from django.urls import path

from .views import HomePage, about, AddPage, ContactFormView, ShowPost, CarsCategory

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CarsCategory.as_view(), name='category'),

]