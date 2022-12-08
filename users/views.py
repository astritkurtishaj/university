from django.shortcuts import render, redirect, reverse
from users.models import User
from django.contrib.auth import authenticate, login, logout


def create_view(request):
    if request.method == 'POST':
        error_messages = {}
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if min(len(password), len(password_confirm)) < 8:
            error_messages['password_error'] = 'password should have more than 7 characters'
        if password != password_confirm:
            error_messages['password_error'] = 'passwords don\'t match'
        if User.objects.filter(email=email).exists():
            error_messages['email_error'] = 'User with this email already exists'
        if error_messages:
            return render(request, 'users/form.html', error_messages)
        User.create_user(email, password)
        return redirect(reverse('departments:home'))
    elif request.method == 'GET':
        return render(request, 'users/form.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect(reverse('departments:home'))
        return render(request, 'users/login.html', context={'error': 'Credentials don\'t match'})
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('users:login'))

