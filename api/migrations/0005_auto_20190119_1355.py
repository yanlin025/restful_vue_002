# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-19 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190119_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='图片'),
        ),
    ]
