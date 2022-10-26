from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.

#HOME VIEW
def home(request):
    return render(request, "pages/home.html")

#REGISTER VIEW
def register(request):
    if request.method == "GET":
        return render(request, "pages/register.html", {
            'form': UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("books")
            except IntegrityError:
                return render(request, "pages/register.html", {
                    'form': UserCreationForm,
                    "error": "User already exists"
                })

        return render(request, "pages/register.html", {
            'form': UserCreationForm,
            "error": "Password do not match"
        })

#SIGNIN VIEW
def signin(request):
    if request.method == "GET":
        return render(request, "pages/signin.html", {
            "form": AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "pages/signin.html", {
                "form": AuthenticationForm,
                'error': "Username or password is incorrect"
            })
        else:
            login(request, user)
            return redirect("home")

#BOOKS VIEW
@login_required
def books(request):
    books = Book.objects.filter(user=request.user)
    return render(request, "pages/books.html", {"books":books})
    
#CREATE VIEW 
@login_required 
def create_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        form.save()
        return redirect ('books')
    return render(request, "pages/edit_book.html", {'form':form})
    
#EDIT VIEW
@login_required
def edit_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid() and request.POST:
        form.save() 
        return redirect('books')
    return render(request, "pages/edit_book.html", {"form":form})

#DELETE VIEW
@login_required
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')

#LOGOUT VIEW
@login_required
def signout(request):
    logout(request)
    return redirect("home")