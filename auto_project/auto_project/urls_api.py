from django.urls import path

from users.views import GetUPDataAPI

urlpatterns = [
    path('get_data_for_user_profile_ajax/', GetUPDataAPI.as_view()),
]
