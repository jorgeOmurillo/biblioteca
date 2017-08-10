from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_author = Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books':num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available, 'num_author': num_author},
    )
