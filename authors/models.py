from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Author(models.Model):

    GENDER_CHOICES = (
        ("male", "male"),
        ("female", "female"),
    )
    MIN_YEAR_BORN = 1800

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=40)
    author_image = models.URLField(blank=True, null=True)
    year_born = models.PositiveIntegerField(
        validators=(MinValueValidator(MIN_YEAR_BORN),), default=MIN_YEAR_BORN
    )
    year_died = models.PositiveIntegerField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    @property
    def life_span(self):
        return (
            f"{self.year_born} - present"
            if self.year_died is None
            else f"{self.year_born} - {self.year_died}"
        )
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @staticmethod
    def name_styling(value:str):
        name = value.split()
        return " ".join(x.lower().capitalize() for x in name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.first_name = self.name_styling(self.first_name)
        self.last_name = self.name_styling(self.last_name)
        self.nationality = self.nationality.lower().capitalize()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.full_name
    