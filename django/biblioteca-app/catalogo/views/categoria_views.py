from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from catalogo.forms.categoria_form import CategoriaForm
from catalogo.models.categoria import Categoria

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria_list.html', {'categorias': categorias})         
                                                                                                                                                                                                                                                                     
def categoria_create(request):
    if request.method=='POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request,
                  'formulario.html',
                  {'form': form})

def categoria_update(request, pk):
    categoria = Categoria.objects.get(pk=pk)
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
        'catalogo/categorias/formulario.html',
        {'form': form}
    )

def categoria_delete(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(
            request, 'Categoría eliminada exitosamente.')
        return redirect('categoria_list')
    return render(request,
                  'catalogo/categorias/categoria_confirm_delete.html',
                  {'categoria': categoria})