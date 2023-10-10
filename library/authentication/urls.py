from django.urls import path, include

from . import views

app_name = 'authentication'

urlpatterns = [
    # Реєстрація
    path('register/', views.register, name='register'),

    # Авторизація
    path('login/', views.login_view, name='login'),

    # Головна
    path('homepage/', views.homepage, name='homepage'),

    # Вихід
    path('logout/', views.logout_view, name='logout'),

    # Показати всіх юзерів
    path('showall/', views.show_all_users, name='showall'),

    # Показати конкретного користувача
    path('show_user/<int:user_id>', views.show_user_info, name='user_info'),
]