# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-03 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autonomy', '0007_auto_20170204_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='petitionfile',
            name='url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
