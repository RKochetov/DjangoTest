from django import forms
from .models import Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Заголовок:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст новости:', required=False, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    is_published = forms.BooleanField(initial=True, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    category = forms.ModelChoiceField(empty_label='Выберите категорию', label='Категория:',
                                      queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-select'}))
