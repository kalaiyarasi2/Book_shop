from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book, Author, Genre
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreListCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

