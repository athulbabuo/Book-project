from django.shortcuts import render,redirect

from .models import Book

# Create your views here.

def CreateBook(request):

    books = Book.objects.all()

    if request.method == "POST":

        title = request.POST.get('title')
        price = request.POST.get('price')

        book = Book(title=title, price=price)
        book.save()

    return render(request, 'book.html',{'books':books})


def listBook(request):

    books=Book.objects.all()

    return render(request, 'listbook.html', {'books':books})

def detailsView(request,book_id):

    book=Book.objects.get(id=book_id)

    return render(request, 'detailsview.html', {'book':book})


def updateBook(request,book_id):

    book=Book.objects.get(id=book_id)

    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        book.title=title
        book.price=price
        book.save()
        return redirect ('/')

    return render(request, 'updateview.html', {'book':book})

def deleteBook(request,book_id):

    book=Book.objects.get(id=book_id)

    if request.method == "POST":

        book.delete()


        return redirect ('/')

    return render(request,'deleteview.html',{'book':book})
