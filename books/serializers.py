from rest_framework import serializers
from .models import Book, Author, Genre, Publisher


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'website', 'email']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'date_of_birth', 'nationality']
        # ← removed 'books' reverse relation (circular + crashes)


class BookSerializer(serializers.ModelSerializer):
    # Read: show nested objects
    author_detail = AuthorSerializer(source='author', read_only=True)
    publisher_detail = PublisherSerializer(source='publisher', read_only=True)

    # Write: accept FK ids
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all()
    )
    publisher = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), allow_null=True, required=False
    )
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_detail',
            'genre', 'publisher', 'publisher_detail',
            'isbn', 'published_date', 'copies_available', 'cover_image'
        ]