from django.contrib import admin
from .models import Author


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ["pk"]
    list_display = ("full_name", "nationality", "gender", "year_born", "year_died")
    list_filter = ("gender", "nationality")
