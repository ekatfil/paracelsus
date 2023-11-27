from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Page, Appointment
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',
                  'password')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email')


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ('birth_date', 'pfp')


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('day',
                  'name',
                  'description')

