from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView # for register and other FBV/CBV
from .views import list_books, LibraryDetailView
from .views import admin_view
from .views import librarian_view
from .views import member_view
from .views import register
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    # Books & Library
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Role-based dashboards
    path("admin-dashboard/", admin_view, name="admin_view"),
    path("librarian-dashboard/", librarian_view, name="librarian_view"),
    path("member-dashboard/", member_view, name="member_view"),

    # Permission-protected book actions
    path("books/add_book/", add_book, name="add_book"),
    path("books/<int:pk>/edit_book/", edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", delete_book, name="delete_book"),

    # Authentication
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", register, name="register"),
]