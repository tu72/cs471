from django.shortcuts import render
from .models import Book
from .models import student
from .models import Address
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
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