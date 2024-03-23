from .models import BookGenre

def book_genre(request):
    return {'book_genre': BookGenre.objects.all()}
