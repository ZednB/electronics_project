from django.contrib import admin
from django.utils.html import format_html

from providers.models import Provider, Product


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'debt', 'supplier_link', 'created_at')
    search_fields = ('name', 'city')
    list_filter = ('country', 'city')
    actions = ['clear_debt']

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="{}">{}</a>', f'/admin/providers/provider/'
                                                      f'{obj.supplier.id}/change/', obj.supplier.name)
        return '-'
    supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        updated_count = queryset.update(debt=0)
        self.message_user(request, f'Задолженность была очищена {updated_count}')
    clear_debt.short_description = 'Очистить задолженность перед поставщиком'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model')
