from rest_framework.generics import CreateAPIView

from voice_cloner_api.apps.accounts.serializers import UserSerializer


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserSerializer
