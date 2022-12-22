from datetime import datetime
from uuid import uuid4

from django.contrib.auth.models import Group
from django.db import models


class ProductsInShop(models.Model):
    id = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        verbose_name='ID',
    )
    product_name = models.CharField(
        help_text='Название продукта',
        max_length=128,
        verbose_name='Название'
    )
    category = models.CharField(
        help_text='Категория продукта',
        max_length=128,
        verbose_name='Категория',
        blank=True,
        null=True
    )
    preview = models.URLField(
        help_text='Ссылка на превью',
        blank=True,
        null=True,
        verbose_name='Превью'
    )
    product_image = models.ImageField(
        upload_to='shop/%Y/%m/%d',
        verbose_name='Фото',
        help_text='Фото продукта',
    )
    product_description = models.CharField(
        blank=True,
        help_text='Описание продукта',
        max_length=512,
        null=True,
        verbose_name='Описание'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        help_text='Группа к которой относится продукт',
        null=True,
        on_delete=models.SET_NULL,
        related_name='plans',
        verbose_name='Группа'
    )
    old_price = models.IntegerField(
        blank=True,
        help_text='Старая цена продукта, если будет скидка',
        null=True,
        verbose_name='Старая цена'
    )
    price = models.IntegerField(
        blank=True,
        help_text='Цена продукта',
        null=True,
        verbose_name='Цена'
    )
    created_at = models.DateTimeField(
        help_text='Дата создания',
        verbose_name='Дата',
        blank=True,
        default=datetime.now
    )

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ["-created_at"]
