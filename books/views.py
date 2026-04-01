from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Book, Genre, Publisher
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer, PublisherSerializer


def home(request):
    return render(request, 'reviews/index.html')   # ← fixed template path


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer