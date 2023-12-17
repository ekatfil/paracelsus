from django.shortcuts import render, redirect
from .forms import UserForm, PageForm, SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login, authenticate
import json
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from main.models import Appointment
# Create your views here.


def index(request):
    content = {
        "title": "Paracelsus",
    }
    return render(request, "main/index.html", content)


def registration(request):
    msg = None
    content = {
        "title": "Регистрация",
    }

    if request.method == "POST":

        form = SignUpForm(request.POST)

        if form.is_valid():

            # Create the user
            form.save()

            msg = 'User created successfully.'
            return redirect('../login')

        else:
            msg = 'Form is not valid'

    else:
        form = SignUpForm()

    content["form"] = form
    content["msg"] = msg

    return render(request, "main/registration.html", content)


def login(request):
    content = {
        "title": "Вход",
    }
    if request.method == "GET":
        form = LoginForm()
        content["form"] = form
        return render(request, "main/login.html", content)

    elif request.method == "POST":
        form = LoginForm(request.POST)
        content["form"] = form
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                dj_login(request, user)
                messages.success(request, f"Hi {username.title()}, welcome back!")
                return redirect("../user/calendar")

        messages.error(request, f"Invalid username or password")
    return render(request, "main/login.html", content)


# @login_required(login_url="main/login")
def user_calendar(request):
    content = {
        "title": "Календарь",
    }
    if request.user.is_authenticated:
        print(request.user)
        return render(request, "main/user-calendar.html", content)
    else:
        return redirect('../../login')


# Пока не разобрались с ошибкой (если я не написала про неё, сигналь), сделала свои вьюшки, а там их отредачим


@login_required
# @transaction.atomic
def testlogin(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        page_form = PageForm(request.POST, instance=request.user.page)
        if user_form.is_valid() and page_form.is_valid():
            user_form.save()
            page_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('main/success.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        page_form = PageForm(instance=request.user.page)

    return render(request, 'main/test_login.html', {
            'user_form': user_form,
            'page_form': page_form
        })

def profile(request):
    content = {
        "title": "Paracelsus",
    }
    return render(request, "main/profile-doctor.html", content)

def patients(request):
    content = {
        "title": "Paracelsus",
    }
    return render(request, "main/patients-doctor.html", content)


def get_appointment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        date = data.get('date')
        appointments = Appointment.objects.filter(day=date, user=request.user)
        data = [{"name": appointment.name, "time": appointment.time, "category": appointment.category} for appointment in appointments]

        return JsonResponse({"appointments": data}, status=200)
    return HttpResponseForbidden("Your not permission to visit this page")

def add_appointment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        date = data.get('date')
        time = data.get('time')
        category = data.get('category')
        text = data.get('text')
        if time:
            Appointment.objects.create(day=date, user=request.user, time=time, category=category, name=text)
        else:
            Appointment.objects.create(day=date, user=request.user, category=category, name=text)

        return JsonResponse({"created": "sucsuss"}, status=200)
    return HttpResponseForbidden("Your not permission to visit this page")

