from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.


# register
def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd["username"], cd["email"], cd["password"])
            user.first_name = cd["first_name"]
            user.last_name = cd["last_name"]
            user.save()
            messages.success(request, "sing in successfully")
            return redirect("home")
    else:
        form = UserRegisterForm()
        return render(request, "register.html", {"form": form})


# Login
def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(request, "you have logged in successfully")
                return redirect("home")
            else:
                messages.error(request, "password or username incorrect")
                return render(request, "login.html", {"form": form})
    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.success(request, "log out successfully")
    return redirect("home")
