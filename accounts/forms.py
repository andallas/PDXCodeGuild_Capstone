from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Permission
from .models import CustomUser, UserInfo


class CustomUserCreationForm(UserCreationForm):
    # default_permissions = []
    # default_permissions.append(Permission.objects.get(name='Can change user')) # In order to edit profile
    # default_permissions.append(Permission.objects.get(name='Can change user info')) # In order to edit profile
    # default_permissions.append(Permission.objects.get(name='Can change post')) # In order to vote on post
    # default_permissions.append(Permission.objects.get(name='Can add comment')) # In order to add comments
    # default_permissions.append(Permission.objects.get(name='Can change comment')) # In order to edit comments

    def save(self, commit=True):
        user = super().save(commit)

        if commit:
            # for permission in self.default_permissions:
            #     user.user_permissions.add(permission)

            userInfo = UserInfo()
            userInfo.user = user
            userInfo.save()

        return user
    
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")