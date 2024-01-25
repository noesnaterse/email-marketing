from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

from .forms import SignUpForm, LogInForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                if user.profile.is_completed():
                    return redirect('home')
                else:
                    return redirect(reverse('account:profile', kwargs={'pk': user.pk}))
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'account/login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse('account:login'))
