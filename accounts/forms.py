from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, UserInfo


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

    def save(self, commit=True):
        user = super().save(commit)
        if commit:
            userInfo = UserInfo()
            userInfo.user = user

            userInfo.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")