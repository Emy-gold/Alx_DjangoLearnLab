from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in list view
    list_filter = ('publication_year',)                     # Filter by publication year
    search_fields = ('title', 'author')                     # Search by title or author

admin.site.register(Book, BookAdmin)
