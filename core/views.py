from django.shortcuts import render, redirect, reverse
from .forms import BaseUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout
from django.db.models import Q
from .forms import KhojForm, ApiForm
from .models import Khoj
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import KhojSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime


def login(request):
    if request.user.is_authenticated:
        return redirect('khoj')
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
            return redirect('login')
    else:
        form = BaseUserForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def khoj(request):
    form = KhojForm()
    context = {
        'form': form
    }
    return render(request, 'khoj.html', context)


def search(request):
    input_values = request.GET.get('input_values')     # take the input_values
    input_values = [int(value.strip()) for value in input_values.split(',')]
    search_value = request.GET.get('search_value')     # take the search_value
    search_value = int(search_value.strip())     # convert search value in integer

    today = datetime.datetime.now()     # current date and time

    date_time = today.strftime('%Y-%m-%d %I:%M:%S')  # convert date time 2021-09-21 12:34:34
    # now input value convert 11, 10, 9, 7, 5, 1, 0 this format
    input_value = ', '.join(str(value) for value in input_values)
    # save the value in database
    khoj_object = Khoj.objects.create(input_values=input_value, user_id=request.user, timestamp=date_time)
    khoj_object.save()
    if search_value in input_values:
        data = "True"
        return JsonResponse({'data': data}, safe=False)
    else:
        data = "False"
        return JsonResponse({'data': data}, safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def KhojApi(request):
    start_datetime = request.POST['start_datetime']
    end_datetime = request.POST['end_datetime']
    user_id = request.user.id
    queryset = Khoj.objects.all()
    if start_datetime and end_datetime and user_id:
        queryset = queryset.filter(timestamp__range=[start_datetime, end_datetime], user_id__id=user_id)
        data = []
        if len(queryset) > 0:
            for pos in queryset:
                item = {
                    'timestamp': pos.timestamp.strftime('%Y-%m-%d %I:%M:%S'),
                    'input_values': pos.input_values,
                }
                data.append(item)
        data = KhojSerializer(data, many=True)
        return Response({
            'status': 'succes',
            'user_id': int(user_id),
            'payload': data.data
        })


def api_form_view(request):
    form = ApiForm()
    context = {
        'form': form
    }
    return render(request, 'api_form.html', context)
