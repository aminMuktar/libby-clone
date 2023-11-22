from rest_framework import viewsets
from rest_framework.response import Response
from catalog.models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# define the viewset as a ModelViewSet
class AuthorViewSet(viewsets.ModelViewSet):
    # specify the queryset as "all authors"
    queryset = Author.objects.all()
    # Asign the serializer class
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
