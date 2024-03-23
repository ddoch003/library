from django import forms
from django.core.exceptions import ValidationError
from .models import Book, BookReadStatus


class TitleFormatMixin:
    @staticmethod
    def title_format(value: str):
        title = value.split()
        return " ".join(x.lower().capitalize() for x in title)

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title:
            formatted_title = self.title_format(title)
            books_with_same_title = Book.objects.filter(
                title__iexact=formatted_title
            ).exclude(pk=self.instance.pk)
            if books_with_same_title.exists():
                raise ValidationError("A book with this title already exists.")
            return formatted_title


class AddBookForm(TitleFormatMixin, forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        widgets = {"book_image": forms.URLInput(attrs={"placeholder": "https://..."})}

        labels = {
            "title": "Title *",
            "genre": "Genre *",
            "year_published": "Year published *",
        }


class EditBookForm(TitleFormatMixin, forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["title"] = self.clean_title()
        return cleaned_data

    def save(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if title:
            self.instance.title = title
        return super().save(*args, **kwargs)


class AddToFavoriteForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())
