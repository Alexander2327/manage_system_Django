# Generated by Django 4.0.4 on 2022-04-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_connectors_options_alter_documents_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osa',
            name='gain',
            field=models.FloatField(verbose_name='Коэфициент усиления'),
        ),
        migrations.AlterField(
            model_name='osa',
            name='gain_flatness',
            field=models.FloatField(verbose_name='Неравномерность усиления'),
        ),
        migrations.AlterField(
            model_name='osa',
            name='noise_figure',
            field=models.FloatField(verbose_name='Шум-фактор'),
        ),
        migrations.AlterField(
            model_name='technicals',
            name='attenuation',
            field=models.FloatField(verbose_name='Полное затухание'),
        ),
        migrations.AlterField(
            model_name='technicals',
            name='i_eol',
            field=models.FloatField(verbose_name='Максимальный ток'),
        ),
        migrations.AlterField(
            model_name='technicals',
            name='i_op',
            field=models.FloatField(verbose_name='Рабочий ток'),
        ),
        migrations.AlterField(
            model_name='technicals',
            name='p_eol',
            field=models.FloatField(verbose_name='Выходная мощность при максимальном тока'),
        ),
        migrations.AlterField(
            model_name='technicals',
            name='p_op',
            field=models.FloatField(verbose_name='Выходная мощность при рабочем тока'),
        ),
        migrations.AlterModelTable(
            name='connectors',
            table='Типы коннекторов',
        ),
        migrations.AlterModelTable(
            name='documents',
            table='Сопроводительные документы',
        ),
        migrations.AlterModelTable(
            name='modifications',
            table='Типы модификаций',
        ),
        migrations.AlterModelTable(
            name='orders',
            table='Номера заказов',
        ),
        migrations.AlterModelTable(
            name='osa',
            table='Результаты анализа спектра',
        ),
        migrations.AlterModelTable(
            name='products',
            table='Изделия',
        ),
        migrations.AlterModelTable(
            name='technicals',
            table='Технические характеристики',
        ),
    ]
