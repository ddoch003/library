from random import sample
from django.shortcuts import render
from django.db.models import Q
from books.models import Book
from authors.models import Author
from .forms import SearchForm


# Create your views here.
def home_page_view(request):
    title = "Libraria 20"

    books = Book.objects.all()
    MAX_RANDOM_OBJECTS = 3
    random_books = []

    if books:
        all_books_list = list(Book.objects.all())
        random_books.extend(sample(all_books_list, min(len(all_books_list), MAX_RANDOM_OBJECTS)))

    context = {"title": title, "books": books, "random_books": random_books}

    if not request.user.is_authenticated:
        return render(request, "home-page-no-user.html", context=context)
    else:
        return render(request, "home-page-with-user.html", context=context)


def search_view(request):
    title = "Search"

    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            author_results = (
                Author.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
            )
            book_results = (
                Book.objects.filter(Q(title__icontains=query))
            )
            results = list(author_results) + list(book_results)
            return render(
                request, "search-results.html", {"results": results, "form": form, "title": title}
            )

    form = SearchForm()
    return render(request, "search-results.html", {"form": form, "title": title})
