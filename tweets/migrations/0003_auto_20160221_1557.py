# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_tweet_tweeter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='posted_at',
            new_name='timestamp',
        ),
    ]
