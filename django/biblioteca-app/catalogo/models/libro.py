from django.db import models
from .categoria import Categoria

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    isbn = models.CharField(max_length=100)
    autores = models.ManyToManyField(
        'Autor',
        related_name='libros',
        blank=True,
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "libros"
        verbose_name = "libro"
        ordering = ['titulo']