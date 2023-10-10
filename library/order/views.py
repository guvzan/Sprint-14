from django.shortcuts import render, redirect
from .models import Order
from book.models import Book

def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'order/all_orders.html', {'orders': orders})


def my_orders(request):
    user = request.user
    my_orders = Order.objects.filter(user=user)
    return render(request, 'order/my_orders.html', {'my_orders': my_orders})


def create_order(request):
    if request.method == 'POST':
        user = request.user
        book_id = request.POST.get('book_id')
        plated_end_at = request.POST.get('plated_end_at')
        book = Book.objects.get(pk=book_id)
        Order.create(user, book, plated_end_at)
        return redirect('all_orders')
    else:
        books = Book.objects.all()
        return render(request, 'order/create_order.html', {'books': books})


def close_order(request, order_id):
    order = Order.get_by_id(order_id)
    if order:
        if request.method == 'POST':
            end_at = request.POST.get('end_at')
            order.update(end_at=end_at)
            return redirect('my_orders')
        else:
            return render(request, 'order/close_order.html', {'order': order})
    else:
        return redirect('my_orders')

