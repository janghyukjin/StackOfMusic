from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User
from bank.models import Bank


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'sex',
            'age',
            'bank_account_number',
            'bank',
        )

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.queryset = forms.ModelChoiceField(queryset=Bank.objects.all())


class UserAuthenticationForm(AuthenticationForm):
    error_messages = '비밀번호가 틀렸습니다.'
