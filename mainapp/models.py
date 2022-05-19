from django.db import models
from django.urls import reverse


class Modifications(models.Model):
    mod = models.CharField(max_length=10, unique=True, verbose_name='Модификация')

    def __str__(self):
        return self.mod

    def get_absolute_url(self):
        return reverse('add_mod')

    class Meta:
        db_table = 'Типы модификаций'
        verbose_name = 'Модификация'
        verbose_name_plural = 'Модификации'


class Products(models.Model):
    serial_num = models.IntegerField(primary_key=True, verbose_name='Серийный номер')
    modification = models.ForeignKey(Modifications, on_delete=models.PROTECT, verbose_name='Модификация')
    con_type = models.ForeignKey('Connectors', on_delete=models.PROTECT, verbose_name='Тип коннектора')
    create_date = models.DateField(verbose_name='Дата производства')
    order = models.ForeignKey('Orders', on_delete=models.PROTECT, verbose_name='Заказ')

    def get_absolute_url(self):
        return reverse('add_product')

    def __str__(self):
        return str(self.serial_num)

    class Meta:
        db_table = 'Изделия'
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'
        ordering = ['serial_num', ]


class Orders(models.Model):
    order = models.CharField(max_length=150, unique=True, verbose_name='Заказ')

    def __str__(self):
        return self.order

    def get_absolute_url(self):
        return reverse('add_ord')

    class Meta:
        db_table = 'Номера заказов'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OSA(models.Model):
    serial_num = models.OneToOneField(Products, on_delete=models.PROTECT, verbose_name='Серийный номер')
    gain = models.FloatField(verbose_name='Коэфициент усиления')
    gain_flatness = models.FloatField(verbose_name='Неравномерность усиления')
    noise_figure = models.FloatField(verbose_name='Шум-фактор')

    def get_absolute_url(self):
        return reverse('add_osa')

    def __str__(self):
        return 'Спектральные характеристики'

    class Meta:
        db_table = 'Результаты анализа спектра'
        verbose_name = 'Анализ Спектра'
        verbose_name_plural = 'Анализ Спектра'
        ordering = ['serial_num', ]


class Technicals(models.Model):
    serial_num = models.OneToOneField(Products, on_delete=models.PROTECT, verbose_name='Серийный номер')
    i_op = models.FloatField(verbose_name='Рабочий ток')
    i_eol = models.FloatField(verbose_name='Максимальный ток')
    p_op = models.FloatField(verbose_name='Выходная мощность при рабочем токе')
    p_eol = models.FloatField(verbose_name='Выходная мощность при максимальном токе')
    attenuation = models.FloatField(verbose_name='Полное затухание')

    def get_absolute_url(self):
        return reverse('add_tech')

    def __str__(self):
        return 'Технические параметры'

    class Meta:
        db_table = 'Технические характеристики'
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
        ordering = ['serial_num', ]


class Connectors(models.Model):
    type = models.CharField(max_length=10, unique=True, verbose_name='Тип коннекторов')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('add_con')

    class Meta:
        db_table = 'Типы коннекторов'
        verbose_name = 'Тип коннектора'
        verbose_name_plural = 'Типы коннекторов'


class Documents(models.Model):
    serial_num = models.OneToOneField(Products, on_delete=models.PROTECT, verbose_name='Серийный номер')
    laser = models.ImageField(upload_to=f'copies/lasers/%Y/%m/%d', verbose_name='Технический паспорт лазера')
    passtopt = models.ImageField(upload_to=f'copies/passports/%Y/%m/%d', verbose_name='Технический паспорт изделия')

    def get_absolute_url(self):
        return reverse('add_doc')

    def __str__(self):
        return 'Документы'

    class Meta:
        db_table = 'Сопроводительные документы'
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['serial_num', ]


class Request(models.Model):
    count = models.IntegerField(verbose_name='Количество изделий')
    count_m12 = models.IntegerField(verbose_name='Количество K25-M12')
    count_n19 = models.IntegerField(verbose_name='Количество K25_M19')
    con_type = models.ForeignKey('Connectors', on_delete=models.PROTECT, verbose_name='Тип коннектора')
    req_date = models.DateField(verbose_name='Дата заявки')
    end_of_date = models.DateField(verbose_name='Дата окончания производства')
    order = models.IntegerField(verbose_name='Номер заказа')
    explanations = models.TextField(verbose_name='Пояснение')
    status = models.BooleanField(verbose_name='Статус', default=False)

    def get_absolute_url(self):
        return reverse('add_req')

    def __str__(self):
        return 'Заявка'

    class Meta:
        db_table = 'Заявки на производство'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['req_date', ]
