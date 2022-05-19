# Generated by Django 4.0.4 on 2022-04-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_orders_alter_products_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='connectors',
            options={'verbose_name': 'Тип коннектора', 'verbose_name_plural': 'Типы коннекторов'},
        ),
        migrations.AlterModelOptions(
            name='documents',
            options={'ordering': ['serial_num'], 'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterModelOptions(
            name='modifications',
            options={'verbose_name': 'Модификация', 'verbose_name_plural': 'Модификации'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='osa',
            options={'ordering': ['serial_num'], 'verbose_name': 'Анализ Спектра', 'verbose_name_plural': 'Анализ Спектра'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['serial_num'], 'verbose_name': 'Изделие', 'verbose_name_plural': 'Изделия'},
        ),
        migrations.AlterModelOptions(
            name='technicals',
            options={'ordering': ['serial_num'], 'verbose_name': 'Характеристика', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.AlterField(
            model_name='connectors',
            name='type',
            field=models.CharField(max_length=10, verbose_name='Тип коннекторов'),
        ),
    ]
