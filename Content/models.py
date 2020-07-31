from django.db import models
import PIL
from django.http import request
from django.urls import reverse


class BookModel(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    Author = models.CharField(max_length=30, verbose_name=u"Автор", blank=True)
    AuthorURL = models.CharField(max_length=500)
    Header = models.CharField(max_length=30, verbose_name=u"Заголовок")
    ShortText = models.CharField(max_length=500, verbose_name=u"Короткий текст")
    Rating = models.FloatField(verbose_name=u"Рейтинг")

    def __str__(self):
        return str(self.book_id)

    def get_absolute_url(self):
        return reverse('Content:Book', args=[self.user_id, self.book_id])


class CommentModel(models.Model):
    Text = models.CharField(max_length=500)
    UserURL = models.CharField(max_length=100)
    UserNickName = models.CharField(max_length=30)
    book_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    isGoodIdea = models.BooleanField(default=False)
    Created = models.DateTimeField(verbose_name=u"Аккаунт создан", auto_now_add=True)
    ReplyToComment = models.OneToOneField('self', on_delete=models.CASCADE, null=True)

    class Meta:
        order_with_respect_to = 'ReplyToComment'


    def __str__(self):
        return str(self.id)

# Create your models here.
