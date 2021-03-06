# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-17 07:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fhiradmin', '0013_auto_20160717_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermedicalprofile',
            name='FullName',
        ),
        migrations.AddField(
            model_name='bloodpressurereading',
            name='User',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Full Name:'),
        ),
        migrations.AddField(
            model_name='bloodpressurereading',
            name='isCaffeineConsumer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], default='No', max_length=20),
        ),
        migrations.AddField(
            model_name='cholesterolreading',
            name='User',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Full Name:'),
        ),
        migrations.AddField(
            model_name='dietintakeperday',
            name='User',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Full Name:'),
        ),
        migrations.AddField(
            model_name='nicotinefood',
            name='User',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Full Name:'),
        ),
        migrations.AddField(
            model_name='physicalactivity',
            name='User',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Full Name:'),
        ),
        migrations.AddField(
            model_name='typeofsmoke',
            name='User',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Full Name:'),
        ),
        migrations.AddField(
            model_name='usermedicalprofile',
            name='User',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Full Name:'),
        ),
        migrations.AlterField(
            model_name='usermedicalprofile',
            name='Age',
            field=models.IntegerField(default='20', verbose_name='Age :'),
        ),
        migrations.AlterField(
            model_name='usermedicalprofile',
            name='FamilyHistory',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], default='No', max_length=20),
        ),
        migrations.AlterField(
            model_name='usermedicalprofile',
            name='HormonalFactor',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], default='No', max_length=20),
        ),
        migrations.AlterField(
            model_name='usermedicalprofile',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Male', max_length=20),
        ),
    ]
