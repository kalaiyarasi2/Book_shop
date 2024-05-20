from django.db import models

# Create your models here.
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title
