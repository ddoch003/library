from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model
from .models import BlogPost, BlogPostComment
from .forms import AddBlogPostCommentForm, AddBlogPostForm, EditBlogPostForm


UserModel = get_user_model()


class PageTitleViewMixin:
    title = ""

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


# Create your views here.
class BlogPageView(PageTitleViewMixin, views.ListView):
    title = "Blog"
    model = BlogPost
    template_name = "blog.html"
    queryset = BlogPost.objects.all().order_by("-pk")
    paginate_by = 3


class AddBlogPostView(PageTitleViewMixin, views.CreateView):
    title = "Add Post"
    model = BlogPost
    form_class = AddBlogPostForm
    template_name = "blog-add.html"
    success_url = reverse_lazy("blog")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EditPostView(PageTitleViewMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    title = "Edit Post"
    model = BlogPost
    form_class = EditBlogPostForm
    pk_url_kwarg = "post_pk"
    template_name = "blog-edit.html"
    success_url = reverse_lazy("blog")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context
    
    def test_func(self):
        post = get_object_or_404(BlogPost, pk=self.kwargs["post_pk"])
        return self.request.user == post.creator


class DeletePostView(PageTitleViewMixin, auth_mixins.UserPassesTestMixin, views.DeleteView):
    title = "Delete Post"
    model = BlogPost
    fields = "__all__"
    pk_url_kwarg = "post_pk"
    template_name = "blog-delete.html"
    success_url = reverse_lazy("blog")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context
    
    def test_func(self):
        post = get_object_or_404(BlogPost, pk=self.kwargs["post_pk"])
        return self.request.user == post.creator or self.request.user.is_superuser or self.request.user.is_staff


class AddBlogPostComment(PageTitleViewMixin, views.CreateView):
    title = "Add Comment"
    model = BlogPostComment
    form_class = AddBlogPostCommentForm
    template_name = "blog-add-comment.html"
    success_url = reverse_lazy("blog")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_pk = self.kwargs.get('post_pk')
        context['post'] = get_object_or_404(BlogPost, pk=post_pk)
        return context
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.to_post_id = self.kwargs['post_pk']
        return super().form_valid(form)
    