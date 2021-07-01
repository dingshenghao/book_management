from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    img = models.CharField(default='', verbose_name='用户头像', max_length=1024)
    role = models.CharField(default=0, verbose_name='用户角色', max_length=1)
    desc = models.TextField(default='', verbose_name='个人简介')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
