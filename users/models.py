from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', default='images/nav/default_user.jpg', verbose_name='Фото')
    photo_background = models.ImageField(upload_to='users/%Y/%m/%d', default='images/nav/default_background.png',
                                         verbose_name='Задний фон')
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name='Город')
    school = models.CharField(max_length=150, blank=True, null=True, verbose_name='Школа')
    vk_link = models.CharField(max_length=150, blank=True, null=True, verbose_name='Ссылка на вк')
    inst_link = models.CharField(max_length=150, blank=True, null=True, verbose_name='Ссылка на инсту')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


def create_profile(**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
