from django.db import models
import PIL
from django.urls import reverse


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    NickName = models.CharField(max_length=30, verbose_name=u"Псевдоним")
    Password = models.CharField(max_length=20, verbose_name=u"Пароль")
    email = models.EmailField(verbose_name=u"Электронная почта")
    Created = models.DateTimeField(verbose_name=u"Аккаунт создан",auto_now_add=True)
    vip_status = models.DateTimeField(verbose_name=u"Подписка",auto_now_add=True)
    Avatar = models.ImageField(blank=True)

    def __str__(self):
        return self.NickName

    def get_absolute_url(self):
        return reverse('Account:Profile', args=[self.user_id])
