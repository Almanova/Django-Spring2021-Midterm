from django.contrib import admin
from .models import Book, Journal


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'num_pages', 'genre', 'created_at')
    list_filter = ('created_at', 'price', 'num_pages')
    search_fields = ('name', 'genre')


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'type', 'publisher', 'created_at')
    list_filter = ('created_at', 'price', 'type')
    search_fields = ('name', 'publisher')
