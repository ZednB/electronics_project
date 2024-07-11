from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from providers.permissions import IsActiveUser
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]
