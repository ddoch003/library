from django.urls import include, path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = (
    path("", login_required(views.AllAuthorsView.as_view()), name="authors"),
    path("add_author/", login_required(views.AuthorAddView.as_view()), name="author add"),
    path("<int:author_pk>/", include([
        path("details/", login_required(views.AuthorDetailsView.as_view()), name="author details"),
        path("edit/", login_required(views.AuthorEditView.as_view()), name="author edit"),
        path("delete/", login_required(views.AuthorDeleteView.as_view()), name="author delete"),
    ])), 
)