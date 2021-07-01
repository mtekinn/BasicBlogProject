from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        return redirect("index")
        messages.info(request, "You have successfuly register")

    context = {
            "form": form
        }
    return render(request, template_name="register.html", context=context)


    """if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            newUser = User(username=username)
            newUser.set_password(password)

            newUser.save()
            login(request, newUser)
            return redirect("index")
        context = {
            "form": form
        }
        return render(request, template_name="register.html", context=context)
    else:
        form  = RegisterForm()
        context = {
            "form": form
        }
        return render(request, template_name="register.html", context=context)"""


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "You have mistake about username or password!")
            return render(request, 'login.html', context=context)

        messages.success(request, "You have successfully logged in")
        login(request, user)
        return redirect("index")

    return render(request, "login.html", context=context)

def logoutUser(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("index")
