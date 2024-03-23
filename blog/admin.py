from django.contrib import admin
from .models import BlogPost, BlogPostComment


# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    ordering = ("pk",)
    list_display = ("title", "creator")
    list_filter = ("creator",)


@admin.register(BlogPostComment)
class BlogPostCommentAdmin(admin.ModelAdmin):
    ordering = ("pk",)
    list_display = ("text", "to_post", "creator",)
    list_filter = ("creator",)
