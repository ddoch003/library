from django.db import models
from django.db import models
from django.contrib.auth import models as auth_models, get_user_model
from accounts.custom_manager import AppUserManager
from .custom_validators import validate_age


# Create your models here.
class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(null=False, blank=False, unique=True)
    date_of_birth = models.DateField(validators=(validate_age,))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email.split("@")[0]


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    favorite_books = models.ManyToManyField("books.Book")

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name and not self.last_name:
            return f"{self.first_name}"
        elif not self.first_name and self.last_name:
            return f"{self.last_name}"
        else:
            return str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.first_name:
            self.first_name = self.first_name.lower().capitalize()
        if self.last_name:
            self.last_name = self.last_name.lower().capitalize()
        return super().save(*args, **kwargs)