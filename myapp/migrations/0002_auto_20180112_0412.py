# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 01:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='band',
            name='user',
            field=models.ManyToManyField(through='myapp.BandUsername', to=settings.AUTH_USER_MODEL),
        ),
    ]
