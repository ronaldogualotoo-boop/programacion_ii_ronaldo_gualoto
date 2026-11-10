from django import forms
from catalogo.models.libro import Libro
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo',
                  'autor',
                  'fecha_publicacion',
                  'categoria',
                  'isbn']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        }