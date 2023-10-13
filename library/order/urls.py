from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('all/', views.all_orders, name='all_orders'),
    path('my/', views.my_orders, name='my_orders'),
    path('create/', views.create_order, name='create_order'),
    path('close/<int:order_id>/', views.close_order, name='close_order'),
    path('edit/<int:order_id>/', views.edit_order, name='edit_order'),
]
