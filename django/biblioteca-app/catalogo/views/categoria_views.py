from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from catalogo.forms.categoria_form import CategoriaForm
from catalogo.models.categoria import Categoria


@login_required
def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        'catalogo/categorias/categoria_list.html',
        {'categorias': categorias},
    )
                                                                                                                                                                                                                                                                     
@login_required
def categoria_create(request):
    if request.method=='POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(
        request,
        'catalogo/categorias/categoria_form.html',
        {'form': form},
    )

@login_required
def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Categoría actualizada exitosamente.'
            )
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(
        request,
        'catalogo/categorias/categoria_form.html',
        {'form': form},
    )

@login_required
@permission_required('catalogo.delete_categoria', raise_exception=True)
def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        try:
            categoria.delete()
        except ProtectedError:
            messages.error(
                request,
                'No se puede eliminar la categoría porque tiene libros asociados.',
            )
        else:
            messages.success(request, 'Categoría eliminada exitosamente.')
        return redirect('categoria_list')
    return render(
        request,
        'catalogo/categorias/categoria_confirm_delete.html',
        {'categoria': categoria},
    )