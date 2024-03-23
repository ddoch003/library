from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from .models import Author
from .forms import AddAuthorForm
from django.contrib.auth import mixins as auth_mixins


class PageTitleViewMixin:
    title = ""

    def get_title(self):
        """
        Return the class title attr by default,
        but you can override this method to further customize
        """
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


# Create your views here.
class AllAuthorsView(PageTitleViewMixin, views.ListView):
    model = Author
    title = "Authors"
    context_object_name = "authors"
    template_name = "authors.html"
    queryset = Author.objects.all().order_by("pk")
    paginate_by = 6


class AuthorAddView(auth_mixins.UserPassesTestMixin, PageTitleViewMixin, views.CreateView):
    model = Author
    title = "Add Author"
    form_class = AddAuthorForm
    template_name = "author-add.html"
    
    def get_success_url(self) -> str:
        return reverse_lazy("author details", kwargs={"author_pk": self.object.pk})

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial["year_born"] = Author.MIN_YEAR_BORN
        return initial
    
    def test_func(self):
        return self.request.user.is_superuser


class AuthorDetailsView(PageTitleViewMixin, views.DetailView):
    model = Author
    pk_url_kwarg = "author_pk"
    template_name = "author-details.html"

    def get_title(self):
        return self.object


class AuthorEditView(
    auth_mixins.UserPassesTestMixin, PageTitleViewMixin, views.UpdateView
):
    model = Author
    title = "Edit Author"
    pk_url_kwarg = "author_pk"
    template_name = "author-edit.html"
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse_lazy("author details", kwargs={"author_pk": self.object.pk})

    def test_func(self):
        return self.request.user.is_superuser


class AuthorDeleteView(auth_mixins.UserPassesTestMixin ,PageTitleViewMixin, views.DeleteView):
    model = Author
    title = "Delete Author"
    pk_url_kwarg = "author_pk"
    template_name = "author-delete.html"
    success_url = reverse_lazy("home page")

    def test_func(self):
        return self.request.user.is_superuser
