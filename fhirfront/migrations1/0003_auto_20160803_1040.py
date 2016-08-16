# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-03 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhirfront', '0002_agerisk_alcoholrisk_bloodpressurerisk_cholesterol_dietrisk_hormonalrisk_physicalactivityrisk_sexrisk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agerisk',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='alcoholrisk',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='dietrisk',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='physicalactivityrisk',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='sexrisk',
            name='categorysex',
        ),
        migrations.RemoveField(
            model_name='weightrisk',
            name='sex',
        ),
        migrations.AddField(
            model_name='agerisk',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Male', max_length=20),
        ),
        migrations.AddField(
            model_name='alcoholrisk',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Male', max_length=20),
        ),
        migrations.AddField(
            model_name='bloodpressurerisk',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Male', max_length=20),
        ),
        migrations.AddField(
            model_name='dietrisk',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Male', max_length=20),
        ),
        migrations.AddField(
            model_name='hormonalrisk',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Female', max_length=20),
        ),
        migrations.AddField(
            model_name='physicalactivityrisk',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Female', max_length=20),
        ),
        migrations.AddField(
            model_name='sexrisk',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Female', max_length=20),
        ),
        migrations.AddField(
            model_name='smokingrisk',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Female', max_length=20),
        ),
        migrations.AddField(
            model_name='weightrisk',
            name='Sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], default='Female', max_length=20),
        ),
    ]