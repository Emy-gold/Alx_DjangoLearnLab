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
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # Role-based dashboards
    path("admin-dashboard/", views.admin_view, name="admin_view"),
    path("librarian-dashboard/", views.librarian_view, name="librarian_view"),
    path("member-dashboard/", views.member_view, name="member_view"),

    # Permission-protected book actions
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),

    # Authentication
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
]