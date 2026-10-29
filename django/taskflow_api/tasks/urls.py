from django.urls import path
from . import views


app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "register",
        views.register,
        name="register"
    ),
    path("aboutme", views.about_me, name="about_me"),
    path(
        "saludo/<str:nombre>/",
        views.greeting,
        name="saludo"
    ),
    path(
        "destinatario/<str:titulo>/<str:nombre>/<str:cargo>/",
        views.destination,
        name="destinatario"
    ),
    path(
        "base-triangulo/<int:base>/<int:altura>/",
        views.base_triangulo,
        name="base-triangulo"
    ),
    path(
        "my-first-template",
        views.my_first_template,
        name="my-first-template"
    ),
    path(
        "tasks/lista",
        views.lista,
        name="task-list"
    ),
    path(
        "tasks/nueva",
        views.task_create,
        name="task-create"
    ),
]