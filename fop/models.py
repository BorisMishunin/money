from celery.tests.app.test_beat import mocked_schedule
from django.db import models

COUNT_METHODS = ((0, 'Фиксированная сумма'), (1, 'Процентом'))

# Create your models here.

class Fops(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")

    class Meta():
        verbose_name = "ФОП"
        verbose_name_plural = "ФОП"

    def __str__(self):
        return self.name


class Payments(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name= "Дата")
    summ_gross = models.FloatField(verbose_name= "Сумма")

    class Meta():
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return self.date

class Taxes(models.Model):
    name = models.CharField("Имя налога", max_length=150)
    count_method = models.IntegerField("Метод расчета", choices=COUNT_METHODS, default=0)
    summ = models.FloatField("Сумма")

    class Meta():
        verbose_name = "Налог"
        verbose_name_plural = "Налоги"

    def __str__(self):
        return  self.name

class Taxe_Payments(models.Model):
    date = models.DateField("Дата", auto_now_add=True)
    date_from = models.DateField("Период с")
    date_to = models.DateField("Период по")
    taxe = models.ForeignKey(Taxes, verbose_name="Налог")
    summ = models.FloatField("Сумма")

    class Meta():
        verbose_name = "Налоговый платеж"
        verbose_name_plural = "Налоговые платежи"

    def __str__(self):
        return self.date


