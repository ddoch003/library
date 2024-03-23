from django.contrib import admin
from .models import Book, BookGenre


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ("pk",)
    list_display = ("title", "book_author", "year_published")
    list_filter = ("genre",)


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    ordering = ("pk",)
