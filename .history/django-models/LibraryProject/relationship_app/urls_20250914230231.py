from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # for register and other FBV/CBV
from .views import list_books, LibraryDetailView
from .views import admin_view

urlpatterns = [
    path("books/", list_books, name="list_books"),  # FBV
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # CBV
    path("admin-dashboard/", views.admin_view, name="admin_view"),
    path("librarian-dashboard/", views.librarian_view, name="librarian_view"),
    path("member-dashboard/", views.member_view, name="member_view"),

    # Authentication
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
]
