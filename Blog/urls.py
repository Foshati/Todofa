from pathlib import Path

from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello_world, name="home"),
    path("profile/", views.profile, name="profile"),
    path("detail/<int:todo_id>/", views.detail, name="details"),
    path("delete/<int:todo_id>/", views.delete, name="delete"),
    path("forms/", views.forms, name="forms"),
    path("update/<int:todo_id>/", views.update, name="update"),
]
