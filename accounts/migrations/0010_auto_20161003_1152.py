# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20160921_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='hosting_booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participation',
            name='transport_booked',
            field=models.BooleanField(default=False),
        ),
    ]
