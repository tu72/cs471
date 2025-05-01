from django.shortcuts import render, redirect
from .models import Book
from .models import student
from .models import student2
from .models import Address
from .models import department
from .models import card
from .models import course
from .forms import BookForm
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.db import transaction
def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')
def html5_links(request):
 return render(request,'bookmodule/links.html')
def text_formatting(request):
 return render(request,'bookmodule/text_formatting.html')
def listing(request):
 return render(request,'bookmodule/listing.html')
def html5_tables(request):
    return render(request, 'bookmodule/html5_tables.html')
def Search(request):
        if request.method == "POST":
            string = request.POST.get('keyword').lower()
            isTitle = request.POST.get('option1')
            isAuthor = request.POST.get('option2')
            # now filter
            books = __getBooksList()
            newBooks = []
            for item in books:
                contained = False
                if isTitle and string in item['title'].lower(): contained = True
                if not contained and isAuthor and string in item['author'].lower():contained = True

                if contained: newBooks.append(item)
            return render(request, 'bookmodule/bookList.html', {'books':newBooks})

        return render(request, 'bookmodule/Search.html')

def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull =
    False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def task1(request):
    mybooks=Book.objects.filter(Q(price__lte='80')) # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def task2(request):
    mybooks = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains="qu") | Q(author__icontains="qu"))) # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def task3(request):
    mybooks = Book.objects.filter(~Q(edition__gt=3) & (~Q(title__icontains="qu") | ~Q(author__icontains="qu"))) # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def task5(request):
    booksnum = Book.objects.count()
    tprice = Book.objects.aggregate(Sum("price"))
    aprice = Book.objects.aggregate(Avg("price", default=0))
    maxprice = Book.objects.aggregate(Max("price"))
    minprice = Book.objects.aggregate(Min("price"))
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task5.html', {'total':booksnum,'tprice':tprice,'aprice':aprice,'maxprice':maxprice,'minprice':minprice})


def task6(request):
    cities = Address.objects.annotate(
        student_count=Count('student')
    ).values('city', 'student_count')
    
    context = {
        'cities': cities
    }

    return render(request, 'bookmodule/task6.html', context)


#lab 10 part 1
def listbooks(request):
            books = Book.objects.all()
            return render(request, 'bookmodule/bookList9.html', {'books':books})

def editbook(request,bookId):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        book = Book.objects.filter(id=bookId).get()
        book.title=title
        book.price=price
        book.save()
        books = Book.objects.all()
        return render(request, 'bookmodule/bookList9.html', {'books':books})

    book = Book.objects.filter(id=bookId).get()
    return render(request, 'bookmodule/editbook.html', {'book':book})

def deletebook(request,bookId):
    Book.objects.filter(id=bookId).delete()
    books = Book.objects.all()
    return render(request, 'bookmodule/bookList9.html', {'books':books})

def addbook(request):
        if request.method == "POST":
            title = request.POST.get('title')
            price = request.POST.get('price')
            book = Book(title=title, price=price)
            book.save()
            books = Book.objects.all()
            return render(request, 'bookmodule/bookList9.html', {'books':books})

        
        return render(request, 'bookmodule/addbook.html')



#lab 10 part 2
def listbooks2(request):
    context = {"books": Book.objects.all()}
    return render(request, "bookmodule/bookList9_2.html", context)

def addbook2(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/lab10_part2/listbooks')
    else:
        form = BookForm()
    
    return render(request, 'bookmodule/addbook_2.html', {'form': form})

def editbook2(request, bookId):
    book = Book.objects.get(id=bookId)
    
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/lab10_part2/listbooks')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookmodule/editbook_2.html', {'form': form, 'book': book})

def deletebook2(request, bookId):
    Book.objects.get(id=bookId).delete()
    return redirect('/books/lab10_part2/listbooks')

#lab 9
def lab9task1(request):
        departments = department.objects.annotate(student_count=Count('student2'))
        return render(request, 'bookmodule/lab9Updated/task1.html', {'departments':departments})

def lab9task2(request):
        courses = course.objects.annotate(student_count=Count('student2'))
        return render(request, 'bookmodule/lab9Updated/task2.html', {'courses':courses})

def lab9task3(request):
        departments = department.objects.annotate(oldest_student_id=Min('student2__id'))
        return render(request, 'bookmodule/lab9Updated/task3.html', {'departments':departments})

def lab9task4(request):
        departments = department.objects.annotate(student_count=Count('student2')).filter(student_count__gte=2).order_by('-student_count')
        return render(request, 'bookmodule/lab9Updated/task4.html', {'departments':departments})
