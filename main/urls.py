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
    path('logout/', main.logout_view, name='logout'),
    path("profile/", main.profile, name="profile"),
    path("profile/patients", main.patients, name="patients"),
    path('api/get-appointment/', main.get_appointment),
    path('api/add-appointment/', main.add_appointment),
    path('api/get-appointment-details/<int:appointment_id>/', main.get_appointment_details, name='get_appointment_details'),
    path('api/update-appointment/<int:appointment_id>/', main.update_appointment, name='update_appointment'),
    path('api/delete-appointment/<int:appointment_id>/', main.delete_appointment, name='delete_appointment'),
    path('group/<int:pk_group>', main.patients_in_group, name="group"),
    path('calendar/<int:pk_user>/', main.calendar_user, name='calendar')
]