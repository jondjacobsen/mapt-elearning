# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='note',
            field=models.CharField(default='Space holder', max_length=400),
            preserve_default=False,
        ),
    ]
