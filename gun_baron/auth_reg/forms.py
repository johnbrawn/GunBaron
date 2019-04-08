from django import forms
from .models import *
from products.models import *


class RegistForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['']
        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'}),
        }


class AuthForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['first_name', 'second_name']
        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['']
        widgets = {
            'comment_text': forms.Textarea(attrs={'rows': 10, 'cols': 20, 'placeholder': 'Добавить коммент'})
        }