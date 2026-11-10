from django.urls import path
from catalogo.views.categoria_views import (
    categoria_delete, categoria_list, categoria_create, categoria_update
)

urlpatterns = [
    path('categorias/',
         categoria_list,
         name='categoria_list'),
    path('categorias/nueva/',
         categoria_create,
         name='categoria_create'),
    path('categorias/<int:pk>/editar/',
         categoria_update,
         name='categoria_update'),
    path('categorias/<int:pk>/eliminar/',
         categoria_delete,
         name='categoria_delete'),
]