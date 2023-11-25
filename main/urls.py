from django.urls import path

import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
    path("registration/", main.registration, name="registration"),
    path("login/", main.login, name="login"),
    path("user/calendar/", main.user_calendar, name="user_calendar"),
]
