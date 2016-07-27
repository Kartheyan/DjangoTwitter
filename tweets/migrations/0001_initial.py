# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=140)),
                ('posted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
