from django.urls import path

import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
]
