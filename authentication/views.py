from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def auth_page(request):
    return HttpResponse("auth page")


def login_user(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index:home")
        else:
            messages.error(request, "Invalid credentials.")

    context = {"page": "login"}
    return render(request, "authentication/login_register.html", context=context)


def logout_user(request):
    print(request)
    logout(request)
    return redirect("index:home")


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("index:home")
        else:
            messages.error(request, "An error occurred during registration")

    form = UserCreationForm()
    context = {"page": "register", "form": form}
    return render(request, "authentication/login_register.html", context=context)


