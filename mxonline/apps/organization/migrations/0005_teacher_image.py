# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-09 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20170808_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='\u5934\u50cf'),
        ),
    ]
