# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-31 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0016_message_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u6d4b\u8bd5\u5de5\u7a0b\u5e08')),
                ('test_time', models.CharField(max_length=20, verbose_name='\u6d4b\u8bd5\u65f6\u95f4')),
                ('comment', models.CharField(max_length=100, verbose_name='\u5907\u6ce8')),
                ('create_time', models.DateTimeField(default=b'2017,08,31 20:1424', verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6d4b\u8bd5\u65e5\u62a5',
                'verbose_name_plural': '\u6d4b\u8bd5\u65e5\u62a5',
            },
        ),
        migrations.RemoveField(
            model_name='job',
            name='test_time',
        ),
        migrations.RemoveField(
            model_name='job',
            name='tester',
        ),
        migrations.AddField(
            model_name='test_report',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Job', verbose_name='\u4efb\u52a1\u540d\u79f0'),
        ),
        migrations.AddField(
            model_name='test_report',
            name='test_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Types', verbose_name='\u4efb\u52a1\u7c7b\u578b'),
        ),
    ]