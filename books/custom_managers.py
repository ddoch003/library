from django.db import models


class BookGenreManager(models.Manager):
    def get_distinct_genres(self):
        return self.get_queryset().distinct("genre")
