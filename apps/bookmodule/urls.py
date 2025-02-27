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
]

