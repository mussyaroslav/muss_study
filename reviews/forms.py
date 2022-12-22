from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['review_content', 'rating']
        widgets = {
            'review_content': forms.Textarea(attrs={"class": "reviews__content__input", "rows": 10}),
        }
