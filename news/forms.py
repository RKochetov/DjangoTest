from django import forms
from .models import Category


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
