from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('home')
    user_form = UserRegisterForm()
    context = {
        'user_form': user_form,
    }
    return render(request, 'register.html', context)


def auth(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                redirect('home')
    form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
