# Generated by Django 4.0.4 on 2022-04-18 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connectors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=5, verbose_name='Тип коннекторов')),
            ],
        ),
        migrations.CreateModel(
            name='Modifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod', models.CharField(max_length=10, verbose_name='Модификация')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('serial_num', models.IntegerField(primary_key=True, serialize=False, verbose_name='Серийный номер')),
                ('create_date', models.DateField(verbose_name='Дата производства')),
                ('order', models.CharField(max_length=150, verbose_name='Заказ')),
                ('con_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.connectors', verbose_name='Тип коннектора')),
                ('modification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.modifications', verbose_name='Модификация')),
            ],
        ),
        migrations.CreateModel(
            name='Technicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_op', models.IntegerField(verbose_name='Рабочий ток')),
                ('i_eol', models.IntegerField(verbose_name='Максимальный ток')),
                ('p_op', models.IntegerField(verbose_name='Выходная мощность при рабочем тока')),
                ('p_eol', models.IntegerField(verbose_name='Выходная мощность при максимальном тока')),
                ('attenuation', models.IntegerField(verbose_name='Полное затухание')),
                ('serial_num', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='mainapp.products', verbose_name='Серийный номер')),
            ],
        ),
        migrations.CreateModel(
            name='OSA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gain', models.IntegerField(verbose_name='Коэфициент усиления')),
                ('gain_flatness', models.IntegerField(verbose_name='Неравномерность усиления')),
                ('noise_figure', models.IntegerField(verbose_name='Шум-фактор')),
                ('serial_num', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='mainapp.products', verbose_name='Серийный номер')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laser', models.ImageField(upload_to='copies/lasers/<django.db.models.fields.related.OneToOneField>', verbose_name='Технический паспорт лазера')),
                ('passtopt', models.ImageField(upload_to='copies/passports/<django.db.models.fields.related.OneToOneField>', verbose_name='Технический паспорт изделия')),
                ('serial_num', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='mainapp.products', verbose_name='Серийный номер')),
            ],
        ),
    ]
