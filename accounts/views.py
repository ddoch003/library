from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views, mixins as auth_mixins, logout, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views
from django.http import HttpResponseForbidden
from .forms import AppUserCreationForm, ProfileEditForm, ProfileDeleteForm
from .models import Profile


UserModel = get_user_model()


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
class AppRegisterView(PageTitleViewMixin, views.CreateView):
    title = "Register"
    form_class = AppUserCreationForm
    template_name = "user-register.html"
    success_url = reverse_lazy("login")


class AppLoginView(PageTitleViewMixin, auth_views.LoginView):
    title = "Login"
    template_name = "user-login.html"


class AppPasswordChangeView(PageTitleViewMixin, auth_views.PasswordChangeView):
    title = "Change Password"
    template_name = "user-password-change.html"
    success_url = reverse_lazy("home page")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Password changed successfully!")
        return response


class ProfileDetailsView(PageTitleViewMixin, views.DetailView):
    title = "Profile Details"
    model = Profile
    pk_url_kwarg = "profile_pk"
    template_name = "profile-details.html"


class ProfileEditView(PageTitleViewMixin, auth_mixins.UserPassesTestMixin, views.UpdateView):
    title = "Edit Profile"
    model = Profile
    form_class = ProfileEditForm
    pk_url_kwarg = "profile_pk"
    template_name = "profile-edit.html"
    
    def get_success_url(self) -> str:
        return reverse_lazy("profile details", kwargs={"profile_pk": self.object.pk})
    
    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs["profile_pk"])
        return self.request.user == profile.user
    

class ProfileDeleteView(PageTitleViewMixin, auth_mixins.UserPassesTestMixin, views.DeleteView):
    title = "Delete Profile"
    model = UserModel
    form_clасс = ProfileDeleteForm
    pk_url_kwarg = "profile_pk"
    template_name = "profile-delete.html"
    success_url = reverse_lazy("home page")

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs["profile_pk"])
        return self.request.user == profile.user


def app_logout_view(request):
    title = "Logout"
    context = {"title": title}

    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect("home page")
        return render(request, "user-logout.html", context)
    else:
        return redirect("home page")
