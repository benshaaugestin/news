# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_news_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='news/src'),
        ),
    ]
