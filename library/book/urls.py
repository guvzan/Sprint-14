from django.urls import path
import book.views as views
from order import views as order_views

app_name = 'book'

urlpatterns = [
    # path('', views.all_books, name='books'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>', views.edit_book, name='edit_book'),
    path('all_books/', views.all_books, name='all_books'),
    # path('<str:param>', views.all_books, name='books_filtered'),
    # path('book_info/<int:id>/', views.book_info, name='book_info'),
    # path('order_book/<int:id>/', order_views.order_book, name='order_book'),
    # path('books_ordered/<int:id>/', views.books_ordered_by_user_id, name='books_ordered'),
]
