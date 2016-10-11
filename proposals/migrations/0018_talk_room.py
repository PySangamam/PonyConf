# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0003_room_label'),
        ('proposals', '0017_talk_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planning.Room'),
        ),
    ]