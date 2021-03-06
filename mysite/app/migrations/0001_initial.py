# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-15 09:48
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
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u54c1\u724c')),
                ('description', models.TextField(blank=True, null=True, verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u54c1\u724c',
                'verbose_name_plural': '\u54c1\u724c',
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u673a\u67dc')),
            ],
            options={
                'verbose_name': '\u673a\u67dc',
                'verbose_name_plural': '\u673a\u67dc',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_number', models.CharField(max_length=32, verbose_name='U\u4f4d')),
                ('name', models.CharField(max_length=64, verbose_name='SN')),
                ('model', models.CharField(max_length=64, verbose_name='\u7c7b\u578b')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='BMC IP')),
                ('mgr_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='\u7ba1\u7406\u7f51IP')),
                ('user', models.CharField(max_length=64, verbose_name='BMC \u8d26\u6237')),
                ('password', models.CharField(max_length=128, verbose_name='BMC \u5bc6\u7801')),
                ('status', models.SmallIntegerField(choices=[(0, 'Normal'), (1, 'Down'), (2, 'No Connect'), (3, 'Error')], verbose_name='\u670d\u52a1\u5668\u72b6\u6001')),
                ('left', models.IntegerField(null=True, verbose_name='\u5269\u4f59\u5929\u6570')),
                ('guarantee_date', models.DateField(verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU')),
                ('hard_disk', models.IntegerField(blank=True, null=True, verbose_name='\u786c\u76d8')),
                ('memory', models.IntegerField(blank=True, null=True, verbose_name='\u5185\u5b58')),
                ('system_user', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7cfb\u7edf\u8d26\u6237')),
                ('system_password', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7cfb\u7edf\u8d26\u6237\u5bc6\u7801')),
                ('description', models.TextField(blank=True, null=True, verbose_name='\u63cf\u8ff0')),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('brand', models.ForeignKey(blank=True, max_length=64, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Brand', verbose_name=b'\xe5\x93\x81\xe7\x89\x8c')),
                ('cabinet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Cabinet', verbose_name=b'\xe6\x9c\xba\xe6\x9f\x9c')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u7ec4\u522b')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u7ec4\u522b',
                'verbose_name_plural': '\u7ec4\u522b',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u673a\u623f')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('contact', models.CharField(max_length=32, verbose_name='\u8054\u7cfb\u4eba')),
                ('telphone', models.CharField(max_length=32, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('address', models.CharField(max_length=128, verbose_name='\u5730\u5740')),
            ],
            options={
                'verbose_name': '\u673a\u623f',
                'verbose_name_plural': '\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7f51\u5361\u7f16\u53f7')),
                ('switch_port', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u4ea4\u6362\u673a\u7aef\u53e3')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Host')),
            ],
            options={
                'verbose_name': '\u7f51\u53e3\u4fe1\u606f',
                'verbose_name_plural': '\u7f51\u53e3\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u4ea4\u6362\u673a')),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cabinet', verbose_name=b'\xe6\x9c\xba\xe6\x9f\x9c')),
            ],
            options={
                'verbose_name': '\u4ea4\u6362\u673a',
                'verbose_name_plural': '\u4ea4\u6362\u673a',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='host_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.HostGroup', verbose_name=b'\xe7\xbb\x84\xe5\x88\xab'),
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.IDC', verbose_name=b'\xe6\x9c\xba\xe6\x88\xbf'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.IDC', verbose_name=b'\xe6\x9c\xba\xe6\x88\xbf'),
        ),
    ]
