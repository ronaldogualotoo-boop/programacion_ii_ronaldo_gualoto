from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("in_progress", "En progreso"),
        ("done", "Completada"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Nave(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_nave = models.TextField(blank=True)
    combustible = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Sensei(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Mision(models.Model):
    sensei = models.ForeignKey(
        Sensei,
        on_delete=models.CASCADE,
        related_name='misiones'  # <- Cambiado para evitar conflicto
    )
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    sensei = models.ForeignKey(
        Sensei,
        on_delete=models.CASCADE,
        related_name='alumnos'
    )
    nombre = models.CharField(max_length=100)
    edad = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    misiones = models.ManyToManyField(Mision, related_name='alumnos')

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfiles/')

    def __str__(self):
        return f"Perfil de {self.alumno.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    titulo = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=300)
    estudiantes = models.ManyToManyField(Estudiante, through='Participacion')

    def __str__(self):
        return self.titulo


class Participacion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE
    )
    actividad = models.ForeignKey(
        Actividad, 
        on_delete=models.CASCADE
    )
    rol = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)