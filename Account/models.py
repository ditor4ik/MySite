from django.db import models


class User(models.Model):
    NickName = models.CharField(max_length=30, verbose_name=u"Псевдоним")
    Password = models.CharField(max_length=20, verbose_name=u"Пароль")
    email = models.EmailField(verbose_name=u"Электронная почта", primary_key=True)
    Created = models.DateTimeField(verbose_name=u"Аккаунт создан",auto_now_add=True)
    vip_status = models.DateTimeField(verbose_name=u"Подписка",auto_now_add=True)
