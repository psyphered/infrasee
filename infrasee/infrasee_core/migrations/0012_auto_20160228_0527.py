# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrasee_core', '0011_remove_port_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='number',
            field=models.IntegerField(),
        ),
    ]
