from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from authors.models import Author
from .custom_managers import BookGenreManager


UserModel = get_user_model()


# Create your models here.
class BookGenre(models.Model):
    GENRE_CHOICE = (
        ("Children's", "Children's"),
        ("Fantasy", "Fantasy"),
        ("Sci-Fi", "Sci-Fi"),
        ("Adventure", "Adventure"),
        ("Drama", "Drama"),
        ("Romance", "Romance"),
        ("Satire", "Satire"),
        ("Utopia", "Utopia"),
        ("Historical", "Historical")
    )
    genre = models.CharField(max_length=15, choices=GENRE_CHOICE)

    objects = BookGenreManager()

    def __str__(self) -> str:
        return self.genre


class Book(models.Model):

    MIN_YEAR_RELEASED = 1900
    MAX_YEAR_RELEASED = 1999

    title = models.CharField(max_length=90, unique=True)
    genre = models.ManyToManyField(BookGenre)
    book_image = models.URLField(blank=True, null=True)
    year_published = models.PositiveIntegerField(
        validators=(
            MinValueValidator(MIN_YEAR_RELEASED),
            MaxValueValidator(MAX_YEAR_RELEASED),
        ),
        default=MIN_YEAR_RELEASED,
    )
    description = models.TextField(blank=True, null=True)
    book_author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, blank=True, null=True
    )
    added_on = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def title_format(value: str):
        title = value.split()
        return " ".join(x.lower().capitalize() for x in title)

    def save(self, *args, **kwargs):
        formatted_title = self.title_format(self.title)
        existing_books = Book.objects.filter(title__iexact=formatted_title).exclude(
            pk=self.pk
        )
        if existing_books.exists():
            raise ValidationError("The book with this title already exists.")
        self.title = formatted_title
        super().save(*args, **kwargs)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class BookReadStatus(models.Model):
    STATUS_CHOICES = (
        ("Have Already Read", "Have Already Read"),
        ("Currently Reading", "Currently Reading"),
        ("Want To Read", "Want To Read"),
    )

    user = models.ForeignKey(UserModel, null=True, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, null=True, blank=True
    )

    class Meta:
        unique_together = ["book", "user"]
