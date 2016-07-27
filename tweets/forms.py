from django.forms import ModelForm
from django import forms

from .models import Tweet


class NewTweetForm(ModelForm):

    class Meta:
        model = Tweet
        fields = ['content']