# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 11:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bands_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name='Фото')),
                ('budget', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='BandUsername',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bands_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Band')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CA_Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bands_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Band')),
            ],
        ),
        migrations.CreateModel(
            name='ConcertAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_CA', models.CharField(max_length=128)),
                ('creation_year', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Sub',
                'verbose_name_plural': 'Subs',
            },
        ),
        migrations.AddField(
            model_name='ca_band',
            name='name_CA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ConcertAgency'),
        ),
        migrations.AddField(
            model_name='band',
            name='user',
            field=models.ManyToManyField(through='myapp.BandUsername', to=settings.AUTH_USER_MODEL),
        ),
    ]
