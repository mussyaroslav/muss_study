from django import forms
from .models import Category, News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title_news', 'content_news', 'category', 'photo_news']
        widgets = {
            'title_news': forms.TextInput(attrs={"class": "add__news__title__input"}),
            'content_news': forms.Textarea(attrs={"class": "add__news__content__input", "rows": 10}),
            'category': forms.Select(attrs={"class": "add__news__select__input"})
        }


class UpdateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title_news', 'content_news', 'category', 'photo_news']
        widgets = {
            'title_news': forms.TextInput(attrs={"class": "edit__news__title__input"}),
            'content_news': forms.Textarea(attrs={"class": "edit__news__content__input", "rows": 10}),
            'category': forms.Select(attrs={"class": "edit__news__select__input"})
        }
