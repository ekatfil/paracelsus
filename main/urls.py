from django.urls import path
from django.contrib.auth.views import LogoutView
import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
    path("registration/", main.registration, name="registration"),
    path("login/", main.login, name="login"),
    path("user/calendar/", main.user_calendar, name="user_calendar"),
    path("testlogin", main.testlogin, name="testlogin"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("profile/", main.profile, name="profile"),
    path("profile/patients", main.patients, name="patients"),
    path('api/get-appointment/', main.get_appointment),
    path('api/add-appointment/', main.add_appointment)
]