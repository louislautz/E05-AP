from django import forms

from .models import Book, Review

class BookForm(forms.ModelForm): 
    class Meta:
        model = Book
        fields = ['name', 'authors', 'year_published']
        labels = {'name':'Name: ', 'authors':'Authors: ', 'year_published':'Published in: '}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'stars', 'unfinished']
        labels = {'text': 'Review ', 'stars': 'Stars ', 'unfinished': 'Unfinished? '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
