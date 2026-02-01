from django.db import models
from django.db.models import ForeignKey, OneToOneField


class Author(models.Model):
    name =models.CharField(max_length=300)
    img_src = models.URLField(blank=True, null=True)
    years_of_age = models.CharField(max_length=10)
    bio = models.TextField()
    works = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'author'
        ordering = ['name']
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
#    img_src = models.URLField(blank=True, null=True)
    Author_name = ForeignKey(Author, on_delete=models.CASCADE, related_name='books' )
    img_src = models.URLField(blank=True, null=True)
    release_date = models.DateField()

    class Meta:
        db_table = 'books'
        ordering = ['title']
    def __str__(self):
        return self.title


class BookDetail(models.Model):
#    name =models.CharField(max_length=300)
#    img_src = models.URLField(blank=True, null=True)
    book = OneToOneField(Book, on_delete=models.CASCADE, related_name='details')
    description = models.TextField

    class Meta:
        db_table = 'book_Details'

    def __str__(self):
        return f'Details of {self.book.title}'






