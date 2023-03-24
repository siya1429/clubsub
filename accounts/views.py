from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        sic = request.POST.get("sic")
        password = request.POST.get("password")
        user = authenticate(username=sic, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        messages.error(request, "Invalid Credentials")
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return render(request, "accounts/logout.html")


@login_required(login_url="login")
def password_reset(request):
    return render(request, "accounts/password_reset.html")


@login_required(login_url="login")
def profile(request):
    user = request.user
    context = {"user": user}
    return render(request, "accounts/profile.html", context)


@login_required(login_url="login")
def profile_edit(request):
    user = request.user
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        user.full_name = name
        user.email = email
        user.save()
        return redirect("profile")
    context = {"user": user}
    return render(request, "accounts/profile_edit.html", context)


def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        sic = request.POST.get("sic")

        user = User(full_name=full_name, email=email, sic=sic)
        user.set_password(password)
        user.save()
        return redirect("login")
    return render(request, "accounts/register.html")
