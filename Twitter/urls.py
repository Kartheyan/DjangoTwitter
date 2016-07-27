"""Twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from django.contrib import admin

from core.views import *
from users.views import *
from interactions.views import *
from tweets.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),  # Core

    url(r'^signup/$', SignUpView.as_view(), name='signup'),  # Users
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),  # Users
    url(r'^logout/$', logout, {'next_page': '/'},  name='logout'),  # Users

    url(r'^follow/(?P<username>\w+)$', FollowView.as_view(), name='follow'),  # Interactions
    url(r'^unfollow/(?P<username>\w+)$', UnfollowView.as_view, name='unfollow'),  # Interactions
    url(r'^block/(?P<username>\w+)/$', BlockView.as_view(), name='block'),  # Interactions
    url(r'^unblock/(?P<username>\w+)/$', UnblockView.as_view(), name='unblock'),  # Interactions

    url(r'^new/tweet$', NewTweetView.as_view(), name='post_tweet'),  # Tweets

    url(r'^(?P<username>\w+)/', include([
        url(r'^$', UserProfileView.as_view(), name='user_profile'),  # Core
        url(r'^tweets/$', UserTweetsView.as_view(), name='user_tweets'),  # Core
        url(r'^following/$', UserFollowingView.as_view(), name='user_following'),  # Core
        url(r'^followers/$', UserFollowersView.as_view(), name='user_followers'),  # Core
    ])),
]
