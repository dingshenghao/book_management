# Generated by Django 2.2.2 on 2021-07-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210701_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.CharField(default='', max_length=1024, verbose_name='用户头像'),
        ),
    ]
