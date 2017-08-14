from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views import generic
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_author = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_books':num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available, 'num_author': num_author, 'num_visits': num_visits},
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    # def get_context_data(self, **kwargs):
        # context = super(BookListView, self).get_context_data(**kwargs)
        # context['some_data'] = 'Data'
        # return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
    paginate_by = 10
