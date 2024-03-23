from django import forms
from django.core.exceptions import ValidationError
from .models import Author


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

        widgets = {
            "author_image": forms.URLInput(attrs={"placeholder": "https://..."})
        }

        labels = {
            "first_name": "First Name *",
            "last_name": "Last Name *",
            "gender": "Gender *",
            "nationality": "Nationality *",
            "year_born": "Year born *",
        }