from django.shortcuts import render

# Create your views here.


def index(request):
    content = {
        "title": "Paracelsus",
    }
    return render(request, "main/index.html", content)


def registration(request):
    content = {
        "title": "Регистрация",
    }
    return render(request, "main/registration.html", content)


def login(request):
    content = {
        "title": "Вход",
    }
    return render(request, "main/login.html", content)


def user_calendar(request):
    content = {
        "title": "Календарь",
    }
    return render(request, "main/user-calendar.html", content)
