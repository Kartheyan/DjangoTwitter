from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps

from tweets.models import Tweet


class User(AbstractUser):

    following = models.ManyToManyField('self', related_name='user_following', symmetrical=False)
    followers = models.ManyToManyField('self', related_name='user_followers', symmetrical=False)
    tweets = models.ManyToManyField('tweets.Tweet', symmetrical=False)

    def get_timeline(self):
        timeline = []
        for user in self.following.all():
            for tweet in user.get_tweets():
                timeline.append(tweet)
        for tweet in self.tweets.all():
            timeline.append(tweet)
        return sorted(timeline, key=lambda user_tweet: user_tweet.timestamp, reverse=True)

    def get_tweets(self):
        return sorted([tweet for tweet in self.tweets.all()], key=lambda user_tweet: user_tweet.timestamp, reverse=True)

    def post_tweet(self, content):
        tweet = Tweet(content=content, tweeter=self)
        tweet.save()
        self.tweets.add(tweet)

    def follow_user(self, user):
        self.following.add(user)
        user.followers.add(self)

    def unfollow_user(self, user):
        self.following.remove(user)
        user.followers.remove(self)
