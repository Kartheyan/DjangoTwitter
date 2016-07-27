from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import NewTweetForm


class NewTweetView(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return redirect('index')
        form = NewTweetForm()
        context = {
            'form': form
        }
        return render(request, 'tweets/new_tweet.html', context)

    def post(self, request):
        if not request.user.is_authenticated():
            return redirect('index')
        form = NewTweetForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            request.user.post_tweet(form.cleaned_data.get('content'))
            return redirect('index')
        return render(request, 'tweets/new_tweet.html', context)
