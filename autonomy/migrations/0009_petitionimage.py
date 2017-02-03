# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-03 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('autonomy', '0008_petitionfile_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetitionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(blank=True, max_length=200)),
                ('file', django_resized.forms.ResizedImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='%Y/%M/%d')),
                ('petition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autonomy.Petition')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]