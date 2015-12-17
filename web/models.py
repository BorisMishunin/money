from django.db import models
import datetime
# Create your models here.


class PaymentsType(models.Model):
    name = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = 'Вид платежа'
        verbose_name_plural = 'Виды платежа'

    def __str__(self):
        return self.name

class Payments(models.Model):
    date = models.DateTimeField('Дата', default=datetime.datetime.now())
    month = models.DateTimeField('Месяц')
    payment = models.ForeignKey(PaymentsType, verbose_name='Вид платежа')
    total = models.IntegerField('Сумма')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return '%s - %s' %(self.mounth,self.payment.namе)

class Goods(models.Model):
    name = models.CharField('Название', max_length=150)
    cost = models.IntegerField('Стоимость', null=True, blank=True)

    class Meta:
        verbose_name = 'Товары или услуги'
        verbose_name_plural = 'Товар или услуга'

    def __str__(self):
        return self.name

class PaymentsTranscript(models.Model):
    payment = models.ForeignKey(Payments, verbose_name='Платеж')
    payment_good = models.ForeignKey(Goods, verbose_name='Товар или услуга')
    quantity = models.IntegerField('Количество')
    price = models.IntegerField('Цена')
    summ = models.IntegerField('Сумма')


