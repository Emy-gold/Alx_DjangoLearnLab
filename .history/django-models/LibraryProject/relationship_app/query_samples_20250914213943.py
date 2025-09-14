from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print("-", book.title)

# Query 2: All books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"\nBooks in {library_name}:")
for book in books_in_library:
    print("-", book.title)

# Query 3: Retrieve the librarian for a library
# Method 1: Using the reverse relation
librarian_via_reverse = library.librarian
print(f"\nThe librarian of {library_name} (via reverse) is {librarian_via_reverse.name}")

# Method 2: Using explicit query with library instance
librarian_via_query = Librarian.objects.get(library=library)
print(f"The librarian of {library_name} (via query) is {librarian_via_query.name}")
