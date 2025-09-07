# Django Admin Configuration for Book Model

## Steps
1. Imported Book model in `bookshelf/admin.py`
2. Created `BookAdmin` class with:
   - list_display: title, author, publication_year
   - list_filter: publication_year
   - search_fields: title, author
3. Registered Book with admin: `admin.site.register(Book, BookAdmin)`
4. Accessed admin interface at `/admin/` and confirmed functionality.
