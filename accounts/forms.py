from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from accounts.models import Profile
from django import forms


UserModel = get_user_model()


class AppUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ("email", "date_of_birth")

        widgets = {
            "date_of_birth": forms.DateInput(attrs={"placeholder": "'YYYY-MM-DD'"}),
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
        )
        if commit:
            profile.save()
        return user


class AppUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = "__all__"


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].widget = forms.HiddenInput()

    class Meta:
        model = Profile
        fields = ("user" ,"first_name", "last_name", "profile_picture")


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"
