# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-07 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20160302_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='register',
        ),
    ]
