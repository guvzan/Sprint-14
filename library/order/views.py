from django.shortcuts import render, redirect

from book.models import Book
from .forms import OrderForm
from .models import Order

def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'order/all_orders.html', {'orders': orders})


def my_orders(request):
    user = request.user
    my_orders = Order.objects.filter(user=user)
    return render(request, 'order/my_orders.html', {'my_orders': my_orders})


def create_order(request):
    if request.method != 'POST':
        form = OrderForm()
    else:
        form = OrderForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('order:all_orders')
    context = {'form': form}
    return render(request, 'order/create_order.html', context)


def edit_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method != 'POST':
        form = OrderForm(instance=order)
    else:
        form = OrderForm(instance=order, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('order:all_orders')
    context = {
        'form': form,
        'order': order,
    }
    return render(request, 'order/edit_order.html', context)


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

