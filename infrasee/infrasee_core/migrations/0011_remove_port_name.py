# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 05:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infrasee_core', '0010_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='port',
            name='name',
        ),
    ]