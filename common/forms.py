from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="Enter an author or a book name")
