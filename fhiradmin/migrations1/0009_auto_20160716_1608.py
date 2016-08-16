# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-16 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhiradmin', '0008_auto_20160716_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermedicalprofile',
            name='HormonalFactor',
            field=models.CharField(default='Nicotine Bubble Gum', max_length=100, verbose_name='HormonalFactor'),
        ),
        migrations.AlterField(
            model_name='usermedicalprofile',
            name='Age',
            field=models.CharField(default='Nicotine Bubble Gum', max_length=100, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='usermedicalprofile',
            name='FamilyHistory',
            field=models.CharField(default='Nicotine Bubble Gum', max_length=100, verbose_name='Family History'),
        ),
        migrations.AlterField(
            model_name='usermedicalprofile',
            name='Sex',
            field=models.CharField(default='Nicotine Bubble Gum', max_length=100, verbose_name='Sex'),
        ),
        migrations.AlterField(
            model_name='usermedicalprofile',
            name='Weight',
            field=models.CharField(default='Nicotine Bubble Gum', max_length=100, verbose_name='Weight'),
        ),
    ]