#БАЗА ДАННЫХ
from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    telegram = models.CharField(max_length=100, verbose_name="Ник в Telegram")
    client_request = models.TextField(verbose_name="Ваш запрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    def __str__(self):
        return f"Заявка от {self.name}"