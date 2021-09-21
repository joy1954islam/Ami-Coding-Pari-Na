from django.shortcuts import render, redirect, reverse
from .forms import BaseUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout
from django.db.models import Q
from .forms import KhojForm
from .models import Khoj
from django.http import JsonResponse


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
    form = KhojForm()
    context = {
        'form': form
    }
    return render(request, 'khoj.html', context)


def search(request):
    input_values = request.GET.get('input_values')
    input_values = [int(value.strip()) for value in input_values.split(',')]
    search_value = request.GET.get('search_value')
    search_value = int(search_value.strip())
    input_value = ', '.join(str(value) for value in input_values)
    khoj_object = Khoj.objects.create(input_values=input_value, user_id=request.user)
    khoj_object.save()
    if search_value in input_values:
        data = "True"
        return JsonResponse({'data': data}, safe=False)
    else:
        data = "False"
        return JsonResponse({'data': data}, safe=False)


