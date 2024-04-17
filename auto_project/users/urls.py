from django.urls import path
from .views import logout_user, RegisterUser, LoginUser

urlpatterns = [
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
]
