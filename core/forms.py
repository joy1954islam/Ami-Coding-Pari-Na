from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Khoj
from datetime import datetime


class BaseUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'username']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username=username).first()
        if user:
            raise forms.ValidationError('You can not use this username')
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email__iexact=email).first()
        if user:
            raise forms.ValidationError('You can not use this email')
        return email


class KhojForm(forms.Form):
    input_values = forms.CharField(max_length=255)
    search_value = forms.CharField(max_length=10)


class ApiForm(forms.Form):
    start_datetime = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M%S'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    end_datetime = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M%S'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        })
    )

