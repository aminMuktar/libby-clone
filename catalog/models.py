from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        help_text='Enter a brief description of the book.')

    def __str__(self):
        """String to represent the model object"""
        return self.title

    class Meta:
        ordering = ['-id']


class Author(models.Model):
    """Model representing an author"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        """String represent the Model object"""
        return f'{self.first_name},{self.last_name}'
