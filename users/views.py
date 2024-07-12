from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from providers.permissions import IsActiveUser
from users.models import User
from users.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]

    def get_permissions(self):
        if self.action == 'create':
            return []
        return [IsAuthenticated(), IsActiveUser()]


class ObtainTokenView(TokenObtainPairView):
    """Возвращает JWT-токен для указанного номера телефона."""

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        if not email:
            return Response({'error': 'Укажите почту.'}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(email=email)
        if created:
            user.set_unusable_password()
            user.save()

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        return Response({
            'refresh': str(refresh),
            'access': str(access_token)
        })
