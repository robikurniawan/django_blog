from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


def loginView(request):
    user = None
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username_login = request.POST['username']
            password_login = request.POST['password']
            user = authenticate(request, username=username_login, password=password_login)

            if user is not None:
                login(request, user)
                messages.success(request, 'Log In successfully.')
                return redirect('../')

            else:
                messages.error(request, 'Error Log In')
        else:
            messages.error(request, 'Error Log In')

    form = AuthenticationForm(request)
    return render(request, 'login.html')


@login_required()
def logoutView(request):
    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)
            return redirect('home')

    return render(request, 'logout.html')
