from django.shortcuts import render, redirect, get_object_or_404
from catalogo.forms.libro_form import LibroForm
from catalogo.models.libro import Libro

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 
                  'catalogo/libros/libro_list.html', 
                  {'libros': libros})

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

def delete_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 
                  'catalogo/libros/confirm_delete.html', 
                  {'libro': libro})