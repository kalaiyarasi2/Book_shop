from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDestroy, AuthorListCreate, AuthorRetrieveUpdateDestroy, GenreListCreate, GenreRetrieveUpdateDestroy

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author-retrieve-update-destroy'),
    path('genres/', GenreListCreate.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroy.as_view(), name='genre-retrieve-update-destroy'),
]

from django.urls import path, include

urlpatterns = [
    path('api/', include('library.urls')),
]
