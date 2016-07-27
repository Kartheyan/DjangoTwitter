from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.apps import apps


class IndexView(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return render(request, 'core/loggedout.html')
        context = {
            'username': request.user.username,
            'timeline': request.user.get_timeline()
        }
        return render(request, 'core/loggedin.html', context)


class UserProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(apps.get_model('users', 'User'), username=username)
        context = {
            'username': user.username,
            'user_tweets': user.get_tweets(),
            'following': len(user.following.all()),
            'followers': len(user.followers.all()),
            #TODO Pass in more profile stuff
        }
        return render(request, 'core/user_profile.html', context)


class UserTweetsView(View):
    def get(self, request, username):
        user = get_object_or_404(apps.get_model('users', 'User'), username=username)
        context = {
            'username': user.username,
            'tweets': user.get_tweets(),
        }
        return render(request, 'core/user_tweets.html', context)


class UserFollowingView(View):
    def get(self, request, username):
        user = get_object_or_404(apps.get_model('users', 'User'), username=username)
        context = {
            'username': user.username,
            'following': user.following.all(),
        }
        return render(request, 'core/user_following.html', context)


class UserFollowersView(View):
    def get(self, request, username):
        user = get_object_or_404(apps.get_model('users', 'User'), username=username)
        context = {
            'username': user.username,
            'followers': user.followers.all(),
        }
        return render(request, 'core/user_followers.html', context)



