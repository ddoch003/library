from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from .models import Book, BookGenre
from .forms import AddBookForm, EditBookForm, AddToFavoriteForm
from django.contrib.auth import mixins as auth_mixins


def is_superuser(user):
    return user.is_superuser


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
class AllBooksView(PageTitleViewMixin, views.ListView):
    title = "All Books"
    model = Book
    template_name = "books.html"
    queryset = Book.objects.all().order_by("pk")
    context_object_name = "books"
    paginate_by = 12


class BookAddView(
    auth_mixins.UserPassesTestMixin, PageTitleViewMixin, views.CreateView
):
    title = "Add Book"
    model = Book
    template_name = "book-add.html"
    form_class = AddBookForm

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial["year_released"] = Book.MIN_YEAR_RELEASED
        return initial

    def get_success_url(self) -> str:
        return reverse_lazy("book details", kwargs={"book_pk": self.object.pk})

    def test_func(self):
        return self.request.user.is_superuser


class BookDetailsView(PageTitleViewMixin ,views.DetailView):
    model = Book
    pk_url_kwarg = "book_pk"
    template_name = "book-details.html"

    def get_title(self):
        return self.object


class BookEditView(
    auth_mixins.UserPassesTestMixin, PageTitleViewMixin, views.UpdateView
):
    title = "Edit Book"
    model = Book
    pk_url_kwarg = "book_pk"
    form_class = EditBookForm
    template_name = "book-edit.html"

    def get_success_url(self) -> str:
        return reverse_lazy("book details", kwargs={"book_pk": self.kwargs["book_pk"]})

    def test_func(self):
        return self.request.user.is_superuser


class BookDeleteView(
    auth_mixins.UserPassesTestMixin, PageTitleViewMixin, views.DeleteView
):
    title = "Delete Book"
    model = Book
    pk_url_kwarg = "book_pk"
    template_name = "book-delete.html"
    success_url = reverse_lazy("home page")

    def test_func(self):
        return self.request.user.is_superuser


class GenreListView(views.ListView):
    template_name = "book-genre-list.html"
    context_object_name = "books"
    paginate_by = 4

    def get_queryset(self):
        genre_pk = self.kwargs["genre_pk"]
        genre = BookGenre.objects.get(pk=genre_pk)
        return genre.book_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genre"] = get_object_or_404(BookGenre, pk=self.kwargs["genre_pk"])
        return context


class AddToFavoriteView(auth_mixins.UserPassesTestMixin, views.View):
    def post(self, request, *args, **kwargs):
        form = AddToFavoriteForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            user = request.user

            if book_id in user.profile.favorite_books.values_list('pk', flat=True):
                user.profile.favorite_books.remove(book_id)
            else:
                user.profile.favorite_books.add(book_id)

        profile_details_url = reverse('profile details', args=[user.profile.pk])
        return redirect(profile_details_url)
    
    def test_func(self):
        return not self.request.user.is_superuser
