from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.apps import apps

User = apps.get_model('users', 'User')


class FollowView(View):
    def get(self, request, username):
        if not request.user.is_authenticated():
            return redirect('index')
        user = get_object_or_404(User, username=username)
        if not request.user == user:
            request.user.follow_user(user)
        return redirect('user_profile', user)


class UnfollowView(View):
    def get(self, request, username):
        if not request.user.is_authenticated():
            return redirect('index')
        user = get_object_or_404(User, username=username)
        if not request.user == user and request.user in user.following.all():
            request.user.unfollow_user(user)
        return redirect('user_profile', user)

    def post(self, request, username):
        pass


class BlockView(View):
    def get(self, request, username):
        pass

    def post(self, request, username):
        pass


class UnblockView(View):
    def get(self, request, username):
        pass

    def post(self, request, username):
        pass


