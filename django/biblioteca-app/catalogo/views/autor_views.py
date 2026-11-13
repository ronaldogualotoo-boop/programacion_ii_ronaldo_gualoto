from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from catalogo.forms.autor_form import AutorForm
from catalogo.models.autor import Autor


@login_required
def autor_list(request):
    autores = Autor.objects.prefetch_related('libros')
    return render(
        request,
        'catalogo/autores/autor_list.html',
        {'autores': autores},
    )


@login_required
def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado exitosamente.')
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(
        request,
        'catalogo/autores/formulario.html',
        {'form': form},
    )


@login_required
def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor actualizado exitosamente.')
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(
        request,
        'catalogo/autores/formulario.html',
        {'form': form},
    )


@login_required
@permission_required('catalogo.delete_autor', raise_exception=True)
def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'Autor eliminado exitosamente.')
        return redirect('autor_list')
    return render(
        request,
        'catalogo/autores/autor_confirm_delete.html',
        {'autor': autor},
    )
