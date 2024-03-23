from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import AppUserCreationForm, AppUserChangeForm
from .models import Profile


UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    list_display = ("pk", "email", "is_staff", "is_superuser", "date_of_birth")
    search_fields = ("email",)
    ordering = ("pk",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("date_of_birth",)}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "groups", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "date_of_birth",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ("pk",)
    list_display = (
        "user_email",
        "first_name",
        "last_name",
    )

    def user_email(self, obj):
        return obj.user.email
