# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-31 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0017_auto_20170831_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_report',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]
