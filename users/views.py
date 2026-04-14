from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        password2 = request.POST.get('password2', '').strip()

        if not username or not password:
            return render(request, 'users/register.html', {
                'error': 'Username va password shart!'
            })

        if password != password2:
            return render(request, 'users/register.html', {
                'error': 'Password mos emas!'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {
                'error': 'Bu username band!'
            })

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')

        return render(request, 'users/login.html', {
            'error': 'Login yoki password xato!'
        })

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')