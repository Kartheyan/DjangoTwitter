from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tweet(models.Model):
    content = models.TextField(max_length=140)

    timestamp = models.DateTimeField(auto_now=True)
    tweeter = models.ForeignKey('users.User')
