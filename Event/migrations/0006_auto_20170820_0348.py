# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 22:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0005_auto_20170820_0135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='priority',
            new_name='preference',
        ),
    ]
