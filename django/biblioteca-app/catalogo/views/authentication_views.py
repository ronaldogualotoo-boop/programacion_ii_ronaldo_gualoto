from django.contrib.auth.views import LoginView, LogoutView


class BibliotecaLoginView(LoginView):
    template_name = 'catalogo/authentication/login.html'


class BibliotecaLogoutView(LogoutView):
    pass
