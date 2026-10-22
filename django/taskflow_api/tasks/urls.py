from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("aboutme", views.about_me, name="aboutme"),
    path("saludo/<str:nombre>/",
         views.greeting, name="saludo"),
    path("destinatario/<str:titulo>/<str:nombre>/<str:cargo>/",
         views.destination, name="destinatario"),
    path("base-triangulo/<int:base>/<int:altura>/",
         views.base_triangulo, name="base-triangulo"),
    path("my-first-template",
     views.my_first_template,
     name="my-first-template"),
]