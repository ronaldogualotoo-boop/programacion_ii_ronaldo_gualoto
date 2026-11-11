from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from catalogo.models.libro import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autores', 'fecha_publicacion', 'categoria', 'isbn']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'fecha_publicacion': 'La fecha de publicación no puede ser futura.',
            'isbn': 'El ISBN debe contener 13 dígitos.',
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo:
            titulo = titulo.strip()
        if not titulo:
            raise forms.ValidationError("Este campo es obligatorio.")
        return titulo

    def clean_fecha_publicacion(self):
        fecha_publicacion = self.cleaned_data.get('fecha_publicacion')
        if fecha_publicacion and fecha_publicacion > timezone.localdate():
            raise ValidationError("La fecha de publicación no puede ser en el futuro.")
        return fecha_publicacion

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if isbn:
            isbn = isbn.strip()
        if not isbn:
            raise forms.ValidationError("Este campo es obligatorio.")
        if len(isbn) != 13 or not isbn.isdigit():
            raise forms.ValidationError("El ISBN debe tener 13 dígitos numéricos.")
        return isbn