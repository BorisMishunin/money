from django.db import models
from django.contrib.auth.models import User

class UserSettings(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь')
    icon = models.ImageField('Аватар', upload_to='users_foto')
    see_itself_notes = models.BooleanField('Отображать только записи пользователя')

    class Meta:
        verbose_name = 'Вид платежа'
        verbose_name_plural = 'Виды платежа'

    def __str__(self):
        return self.user.name
