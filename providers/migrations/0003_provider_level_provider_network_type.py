# Generated by Django 5.0.7 on 2024-07-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_alter_provider_debt'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='Уровень иерархии'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider',
            name='network_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], default=0, verbose_name='Выбор поставщика'),
            preserve_default=False,
        ),
    ]