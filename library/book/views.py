from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def all_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'book/all_books.html', context)

def add_book(request):
    if request.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:all_books')
    context = {'form': form}
    return render(request, 'book/add_book.html', context)


def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method != 'POST':
        form = BookForm(instance=book)
    else:
        form = BookForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:all_books')
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'book/edit_book.html', context)