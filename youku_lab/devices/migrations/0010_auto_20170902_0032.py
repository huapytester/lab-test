# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-02 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0009_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='borrower',
            field=models.CharField(max_length=20, verbose_name='\u501f\u7528\u4eba'),
        ),
    ]
