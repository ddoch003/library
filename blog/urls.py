from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = (
    path("", login_required(views.BlogPageView.as_view()), name="blog"),
    path("add_post/", login_required(views.AddBlogPostView.as_view()), name="blog add"),
    path("<int:post_pk>/", include([
        path("edit/", login_required(views.EditPostView.as_view()), name="blog edit"),
        path("delete/", login_required(views.DeletePostView.as_view()), name="blog delete"),
        path("add_comment/", login_required(views.AddBlogPostComment.as_view()), name="blog comment add")
    ])),
)