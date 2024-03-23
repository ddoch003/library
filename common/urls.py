from django.urls import include, path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = (
    path("", views.home_page_view, name="home page"),
    path("search/", login_required(views.search_view), name="search")
)
