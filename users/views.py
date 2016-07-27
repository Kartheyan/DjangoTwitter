from django.shortcuts import render, redirect
from django.views.generic import View

from .models import User
from .forms import UserCreationForm
# Create your views here.


class SignUpView(View):
    def get(self, request):
        if not request.user.is_authenticated():
            form = UserCreationForm()
            context = {
                'form': form
            }
            return render(request, 'users/signup.html', context)
        return redirect('index')

    def post(self, request):
        if not request.user.is_authenticated():
            form = UserCreationForm(request.POST)
            context = {
                'form': form
            }
            if form.is_valid():
                User.objects.create_user(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'), email=form.cleaned_data.get('email'))
                return redirect('login')
            return render(request, 'users/signup.html', context)
        return redirect('index')



