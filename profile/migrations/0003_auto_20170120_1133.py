# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20170120_1127'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserVehicleInfo',
            new_name='UserInfo',
        ),
    ]
