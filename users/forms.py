from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from .models import User


# Form Validators

def UsernameValidator(value):
    forbidden_usernames = ['admin']
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('Please enter a valid username')
    elif User.objects.filter(username__iexact=value).exists() or value.lower() in forbidden_usernames:
        raise ValidationError('Username taken')


def EmailValidator(value):
    forbidden_domains = ['']
    if value.split('@')[1] in forbidden_domains:
        raise ValidationError('Emails on that domain is not allowed')
    elif User.objects.filter(email__iexact=value).exists():
        raise ValidationError('A user with that email already exists')


class UserCreationForm(ModelForm):
    username = forms.CharField(max_length='30', required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(UsernameValidator)
        self.fields['email'].validators.append(EmailValidator)

    def clean(self):
        super(UserCreationForm, self).clean()
        if self.cleaned_data.get('password') != self.cleaned_data.get('confirm_password'):
            self._errors['password'] = self.error_class(['Passwords dont match'])
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
