# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-06 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_fss', '0002_auto_20160306_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='id',
        ),
        migrations.AlterField(
            model_name='inscription',
            name='num',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
