from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links/', views.html5_links, name='html5_links'),
 path('html5/text/formatting', views.text_formatting, name='text_formatting'),
 path('html5/listing',views.listing, name="listing"),
 path('html5/tables', views.html5_tables, name='html5_tables'),
 path('search', views.Search, name='Search'),
 path('simple/query', views.simple_query, name='simple_query'),
 path('complex/query', views.complex_query, name='complex_query'),
  path('lab8/task1', views.task1, name='task1'),
  path('lab8/task2', views.task2, name='task2'),
  path('lab8/task3', views.task3, name='task3'),
  path('lab8/task4', views.task4, name='task4'),
  path('lab8/task5', views.task5, name='task5'),
path('lab8/task6', views.task6, name='task6'),
path('lab9_part1/listbooks', views.listbooks, name='listbooks'),
path('lab9_part1/editbook/<int:bookId>', views.editbook, name='editbook'),
path('lab9_part1/deletebook/<int:bookId>', views.deletebook, name='deletebook'),
path('lab9_part1/addbook', views.addbook, name='addbook'),
]

