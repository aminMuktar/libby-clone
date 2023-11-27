from django.db import models
from django.conf import settings
from catalog.models import Book


class Review(models.Model):
    """
    Represents a rating for one book.
    :book: Book review is associated with.
    :value: Rating value (1-5 stars).
    :comment: The reviewer's comment. 
    """
    RATING_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             default=1, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Publication Date')
    comment = models.TextField(max_length=1024)
    value = models.IntegerField(choices=RATING_CHOICES, default=1)

    def __str__(self):
        return '{0}/{1}-{2}'.format(self.book.title, self.user.username, self.value)

    class Meta:
        verbose_name = "Book Review"
        verbose_name_plural = "Book Reviews"
        ordering = ['-pub_date']
