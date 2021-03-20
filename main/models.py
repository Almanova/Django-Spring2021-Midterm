from django.db import models

from utils import constants


class BookJournalBase(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    price = models.PositiveIntegerField(default=0, verbose_name='Price')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Book(BookJournalBase):
    num_pages = models.PositiveIntegerField(default=0, verbose_name='Number of pages')
    genre = models.CharField(max_length=100, verbose_name='Genre')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Journal(BookJournalBase):
    type = models.CharField(choices=constants.JOURNAL_TYPES,
                            default=constants.BULLET,
                            max_length=100,
                            verbose_name='Journal type')
    publisher = models.CharField(max_length=100,
                                 verbose_name='Publisher')

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
