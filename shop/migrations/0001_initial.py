# Generated by Django 4.1.4 on 2022-12-22 14:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsInShop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='Название продукта', max_length=128, verbose_name='Название')),
                ('category', models.CharField(blank=True, help_text='Категория продукта', max_length=128, null=True, verbose_name='Категория')),
                ('preview', models.URLField(blank=True, help_text='Ссылка на превью', null=True, verbose_name='Превью')),
                ('product_image', models.ImageField(help_text='Фото продукта', upload_to='shop/%Y/%m/%d', verbose_name='Фото')),
                ('product_description', models.CharField(blank=True, help_text='Описание продукта', max_length=512, null=True, verbose_name='Описание')),
                ('old_price', models.IntegerField(blank=True, help_text='Старая цена продукта, если будет скидка', null=True, verbose_name='Старая цена')),
                ('price', models.IntegerField(blank=True, help_text='Цена продукта', null=True, verbose_name='Цена')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='Дата создания', verbose_name='Дата')),
                ('group', models.ForeignKey(blank=True, help_text='Группа к которой относится продукт', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plans', to='auth.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-created_at'],
            },
        ),
    ]
