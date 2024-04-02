import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
django.setup()

from django.db.models import Q
from authors.models import Author
from books.models import Book
