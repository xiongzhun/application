# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-15 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181015_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='info',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='\u73af\u5883\u4fe1\u606f'),
        ),
        migrations.AddField(
            model_name='host',
            name='popurse',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='\u7528\u9014'),
        ),
    ]