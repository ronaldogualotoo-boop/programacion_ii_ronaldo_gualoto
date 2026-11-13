from django.urls import path

from catalogo.views.autor_views import (
    autor_create,
    autor_delete,
    autor_list,
    autor_update,
)

urlpatterns = [
    path('autores/', autor_list, name='autor_list'),
    path('autores/nuevo/', autor_create, name='autor_create'),
    path('autores/<int:pk>/editar/', autor_update, name='autor_update'),
    path('autores/<int:pk>/eliminar/', autor_delete, name='autor_delete'),
]
