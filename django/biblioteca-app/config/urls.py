from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('admin/', admin.site.urls),
    path('inicio/', include('catalogo.urls.home_urls')),
    path('catalogo/', include('catalogo.urls.categoria_urls')),
    path('catalogo/', include('catalogo.urls.libro_urls')),
    path('catalogo/', include('catalogo.urls.autor_urls')),
    path('cuentas/', include('catalogo.urls.authentication_urls')),
]