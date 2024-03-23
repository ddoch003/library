from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = (
    path("register/", views.AppRegisterView.as_view(), name="register"),
    path("login/", views.AppLoginView.as_view(), name="login"),
    path("logout/", views.app_logout_view, name="logout"),

    path("change_password/", views.AppPasswordChangeView.as_view(), name="password change"),
    path("reset_password/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path("profile/<int:profile_pk>/", include([
        path("", login_required(views.ProfileDetailsView.as_view()), name="profile details"),
        path("edit/", views.ProfileEditView.as_view(), name="profile edit"),
        path("delete/", views.ProfileDeleteView.as_view(), name="profile delete"),
    ]))
)
