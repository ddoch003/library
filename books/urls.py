from django.urls import include, path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = (
    path("all_books/", views.AllBooksView.as_view(), name="all books"),
    path("add_book/", login_required(views.BookAddView.as_view()), name="book add"),
    path("<int:book_pk>/", include([
        path("details/", login_required(views.BookDetailsView.as_view()), name="book details"),
        path("edit/", login_required(views.BookEditView.as_view()),name="book edit"),
        path("delete/", login_required(views.BookDeleteView.as_view()),name="book delete"),
    ])),
    path("genre/<int:genre_pk>/", login_required(views.GenreListView.as_view()), name="genre"),
    path('add-to-favorites/', login_required(views.AddToFavoriteView.as_view()), name='add to favorites'),
)