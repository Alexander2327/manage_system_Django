# Generated by Django 4.0.4 on 2022-05-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='count_n19',
            field=models.IntegerField(verbose_name='Количество K25-M19'),
        ),
    ]