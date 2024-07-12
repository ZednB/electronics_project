from rest_framework import serializers

from providers.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'debt', 'created_at',
                  'level', 'network_type']
        read_only_fields = ['debt', 'created_at', 'level']
