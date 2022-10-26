from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("books", views.books, name = "books"),
    path("register", views.register, name = "register"),
    path("signin/", views.signin, name = "signin"),
    path("logout/", views.signout, name = "logout"),
    path("books/create", views.create_book, name = "create_book"),
    path("books/edit", views.edit_book, name = "edit_book"),
    path("delete/<int:id>", views.delete_book, name = "delete_book"),
    path("books/edit_book/<int:id>", views.edit_book, name = "edit_book"),
]
