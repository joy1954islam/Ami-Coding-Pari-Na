from django.shortcuts import render, redirect, reverse
from .forms import BaseUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout
from django.db.models import Q


def login(request):
    if request.method == "POST":
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        user = User.objects.filter(
            Q(username=username_or_email) |
            Q(email=username_or_email)
        ).first()
        if user:
            user_authentication = authenticate(request, username=user, password=password)
            if user_authentication is not None:
                auth_login(request, user_authentication)
                return redirect(reverse('khoj'))
            else:
                message = "Your Username or Email And Password Is Wrong"
                context = {
                    'message': message,
                }
                return render(request, 'login.html', context=context)
        else:
            message = "Your Username or Email And Password Is Wrong"
            context = {
                'message': message,
            }
            return render(request, 'login.html', context=context)
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = BaseUserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = BaseUserForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')


def khoj(request):
    form = None
    context = {
        'form': form
    }
    return render(request, 'khoj.html', context)
