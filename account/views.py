from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LogInForm, ProfileForm, SignUpForm


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
                    return redirect(reverse('account:profile'))
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'account/login.html', {'form': form, 'error': error})


@login_required(login_url="/user/login")
def log_out(request):
    logout(request)
    return redirect(reverse('account:login'))


@login_required(login_url="/user/login")
def profile(request, id: str):
    user = request.user
    error = False
    if request.method == "POST":
        # Save the form
        form = ProfileForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data["bio"]
            birth_date = form.cleaned_data["birth_date"]
            profile = user.profile
            profile.bio = bio
            profile.birth_date = birth_date
            profile.save()
            return redirect('home')
    else:
        profile = user.profile
        form = ProfileForm()

    return render(request, 'account/profile.html', {'form': form, 'error': error, 'user': user, })
