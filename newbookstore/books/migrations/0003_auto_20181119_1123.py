# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 11:23
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20181115_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/atguigu/rookie/newbookstore/static'), upload_to='books', verbose_name='商品图片'),
        ),
    ]
