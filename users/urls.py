from django.urls import path

from users.apps import UsersConfig
from users.views import ObtainTokenView

app_name = UsersConfig.name

urlpatterns = [
    path('auth/token/', ObtainTokenView.as_view(), name='obtain_token')
]