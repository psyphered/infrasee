# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrasee_core', '0007_auto_20160222_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='environments',
            field=models.ManyToManyField(blank=True, null=True, to='infrasee_core.Environment'),
        ),
    ]
