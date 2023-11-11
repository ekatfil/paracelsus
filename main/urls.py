from django.urls import path

import main.views as main

app_name = "main"

urlpatterns = [
    path("", main.index, name="index"),
    path("create_user/", main.create_user),
    path("edit/<int:id>/", main.edit),
    path("delete/<int:id>/", main.delete),
]
