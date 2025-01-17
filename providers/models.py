from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Provider(models.Model):

    NetworkLevel = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=150, verbose_name='Название')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, related_name='clients',
                                 verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    level = models.PositiveIntegerField(editable=False, verbose_name='Уровень иерархии')
    network_type = models.PositiveSmallIntegerField(choices=NetworkLevel, verbose_name='Выбор поставщика')

    def save(self, *args, **kwargs):
        if self.network_type == 0:
            self.level = 0
        elif self.network_type == 1 and self.supplier and self.supplier.network_type == 0:
            self.level = 1
        elif self.network_type == 2 and self.supplier and self.supplier.network_type in [0, 1]:
            self.level = 2
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название продукта')
    model = models.CharField(max_length=150, verbose_name='Модель продукта')
    release_date = models.DateField(verbose_name='Дата релиза')
    provider = models.ForeignKey(Provider, related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Поставщик')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
