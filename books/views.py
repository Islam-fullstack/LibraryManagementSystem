from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import Author, Book, Genre, Publisher
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer, PublisherSerializer
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def member_list(request):
    from members.models import Member
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

def borrowing_list(request):
    from borrowing.models import Borrowing
    borrowings = Borrowing.objects.all()
    return render(request, 'borrowing/borrowing_list.html', {'borrowing': borrowings})

def member_list(request):
    from members.models import Member
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

def staff_list(request):
    from staff.models import Staff
    staffs = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {'staff': staffs})

def review_list(request):
    from reviews.models import Review
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})