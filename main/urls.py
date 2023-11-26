from django.urls import path

import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
    path("registration/", main.registration, name="registration"),
    # path("login/", main.login, name="login"),
    path("user/calendar/", main.user_calendar, name="user_calendar"),
    path("testlogin", main.testlogin, name="testlogin"),
    path("register", main.register_user, name="register"),
    path("betalogin", main.betalogin, name="betalogin")
]
