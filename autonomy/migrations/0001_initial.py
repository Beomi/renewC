# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 10:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('valid_until', models.DateField(default=datetime.date.today)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PetitionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('petition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autonomy.Petition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PetitionProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('petition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autonomy.Petition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.PositiveIntegerField(default=0)),
                ('paid_until', models.DateField(default=datetime.date.today)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoteChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('choice', models.CharField(max_length=200)),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autonomy.Vote')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoteComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autonomy.Vote')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
