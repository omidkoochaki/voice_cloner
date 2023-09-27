from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from voice_cloner_api.apps.accounts.views import UserRegistrationAPIView

urlpatterns = [
    path('login/', obtain_auth_token),
    path('register/', UserRegistrationAPIView.as_view()),
]
