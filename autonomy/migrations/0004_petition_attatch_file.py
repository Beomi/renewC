# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('autonomy', '0003_remove_userinfo_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='attatch_file',
            field=models.FileField(blank=True, storage=gdstorage.storage.GoogleDriveStorage(), upload_to='/files'),
        ),
    ]
