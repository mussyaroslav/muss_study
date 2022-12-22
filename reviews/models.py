from django.contrib.auth.models import User
from django.db import models


class Reviews(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    review_content = models.TextField(blank=False, verbose_name='Отзыв')
    review_created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    rating = models.IntegerField(default=5, verbose_name='Рейтинг')

    def __int__(self):
        return self.user

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-review_created_at']
