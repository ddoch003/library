from django import forms
from django.contrib.auth import get_user_model
from .models import BlogPost, BlogPostComment


UserModel = get_user_model


class AddBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "text"]
        widgets = {
            "title": forms.TextInput(),
            "text": forms.Textarea(
                attrs={
                    "placeholder": "Add your text here...",
                }
            ),
        }


class EditBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "text"]


class AddBlogPostCommentForm(forms.ModelForm):
    class Meta:
        model = BlogPostComment
        fields = ["text"]
        