from django import forms
from .models import User


class PersonCreateView(forms.Form):
    NickName = forms.CharField(max_length=30, label="Псевдоним", widget=forms.TextInput(attrs={'placeholder': 'YourNickName1234', 'class': 'NickNameJQ'}))
    email = forms.CharField(max_length=50, label='Электронная почта', widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com', 'class': 'emailJQ'}))
    Password = forms.CharField(max_length=20, label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Password1234', 'class': 'PasswordJQ'}))
    Password2 = forms.CharField(max_length=20, label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'Password2JQ'}))



class SignInView(forms.Form):
    NickName = forms.CharField(max_length=30, label="Псевдоним", widget=forms.TextInput(attrs={'placeholder': 'YourNickName1234', 'class': 'NickNameJQ'}))
    Password = forms.CharField(max_length=20, label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Password1234', 'class': 'PasswordJQ'}))
