from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.password)

    class Meta:
        model = User
        fields = ['username', 'password']
