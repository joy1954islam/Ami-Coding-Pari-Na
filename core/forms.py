from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
