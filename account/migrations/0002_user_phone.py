# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Phone',
            field=models.TextField(blank=True, null=True),
        ),
    ]
