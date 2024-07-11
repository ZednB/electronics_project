from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from providers.models import Provider
from providers.permissions import IsActiveUser
from providers.serializers import ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']
    permission_classes = [IsAuthenticated, IsActiveUser]
