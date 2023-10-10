from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import CustomUser


def homepage(request):
    return render(request, 'home/home.html')


def register(request):
    """
    Реєстрація користувача за повним іменем, поштою та паролем.
    :param request:
    :return:
    """
    if request.method == 'POST':
        user_role = 1 if request.POST['role'] == 'librarian' else 0

        user_manager = CustomUser.objects

        user_manager.create_user(
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            middle_name=request.POST['middle_name'],
            last_name=request.POST['last_name'],
            role=user_role,
        )
        return redirect('authentication:homepage')
    return render(request, 'registration/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('authentication:homepage')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'registration/login.html')


@login_required()
def logout_view(request):
    logout(request)
    return redirect('authentication:homepage')


@login_required()
def show_all_users(request):
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'home/all_users.html', context)


@login_required()
def show_user_info(request, user_id):
    user = CustomUser.objects.filter(id=user_id)
    context = {
        'my_user': user[0] if user else None,
    }
    return render(request, 'home/user_info.html', context)
