# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-30 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0014_auto_20170830_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='test_time',
            field=models.CharField(max_length=20, verbose_name='\u6d4b\u8bd5\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='job',
            name='work_time',
            field=models.CharField(max_length=30, verbose_name='\u9884\u8ba1\u5de5\u65f6'),
        ),
    ]
