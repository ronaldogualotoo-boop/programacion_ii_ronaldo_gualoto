from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from catalogo.forms.libro_form import LibroForm
from catalogo.models.categoria import Categoria
from catalogo.models.libro import Libro


@login_required
def libro_list(request):
    pista = request.GET.get('pista', '').strip()
    categoria_id = request.GET.get('categoria', '')
    libros = Libro.objects.prefetch_related('autores')

    if pista:
        libros = libros.filter(
            Q(titulo__icontains=pista)
            | Q(autores__nombre__icontains=pista)
            | Q(autores__apellido__icontains=pista)
            | Q(categoria__nombre__icontains=pista)
        ).distinct()

    if categoria_id.isdigit():
        libros = libros.filter(categoria_id=categoria_id)
    else:
        categoria_id = ''

    return render(request, 
                  'catalogo/libros/libro_list.html', 
                  {
                      'libros': libros,
                      'categorias': Categoria.objects.all(),
                      'pista': pista,
                      'categoria_id': categoria_id,
                  })

@login_required
def create_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm()
    return render(request, 
                  'catalogo/libros/formulario.html', 
                  {'form': form})

@login_required
def update_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro_list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 
                  'catalogo/libros/formulario.html', 
                  {'form': form})

@login_required
@permission_required('catalogo.delete_libro', raise_exception=True)
def delete_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 
                  'catalogo/libros/libro_confirm_delete.html',
                  {'libro': libro})